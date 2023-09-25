from pyspark.sql import SparkSession
from pyspark.sql.functions import split, col,udf
from textblob import TextBlob
from pyspark.sql.types import StringType


spark = SparkSession.builder\
    .appName("Streaming")\
        .config("spark.sql.streaming.schemaInference", "true")\
            .getOrCreate()


kafka_bootstrap_servers = "localhost:9092" 
kafka_topics = "orders"
data_storage_path="/jenly/projects/sentimentAnalysis/tweets"
kafka_source = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer") \
    .option("subscribe", "orders") \
    .load()


def getSentiment(text):
    analysis = TextBlob(text)
    return "Positive" if analysis.sentiment.polarity > 0 else "Negative" if analysis.sentiment.polarity < 0 else "Neutral"
sentiment_udf = udf(getSentiment, StringType())


# Split the Kafka message values and select the columns
split_data = kafka_source.select(split(col("value"), ",").alias("split_data"))
kafka_df_with_columns = split_data.select(
    col("split_data")[0].alias("tweet_id"),
    col("split_data")[1].alias("username"),
    "split_data"
)

def concatenate_elements(arr):
    return arr[2]

concat_udf = udf(concatenate_elements, StringType())

kafka_df_with_columns = kafka_df_with_columns.withColumn("tweet_text", concat_udf(kafka_df_with_columns["split_data"]))
kafka_df_with_columns = kafka_df_with_columns.drop("split_data")
kafka_df_with_columns = kafka_df_with_columns.withColumn("sentiment",sentiment_udf(kafka_df_with_columns["tweet_text"]))

def write_to_hdfs(df, epoch_id):
    df.write\
        .mode("append")\
            .csv(data_storage_path)

# Apply the write_to_hive function to each micro-batch
kafka_df_with_columns.writeStream \
    .foreachBatch(write_to_hdfs) \
    .start() \
    .awaitTermination()

spark.stop()
