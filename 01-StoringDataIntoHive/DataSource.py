from pyspark.sql import SparkSession
from pyspark.sql.functions import split, col

spark = SparkSession.builder \
    .appName("SparkStreamingToHive") \
    .enableHiveSupport() \
    .getOrCreate()

kafka_bootstrap_servers = "localhost:9092" 
kafka_topics = "orders"
base_storage_path = "/home/projects/SentimentAnalysis"
hive_table = "STMTDATA.tweet_data"

kafka_source = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer") \
    .option("subscribe", "orders") \
    .load()

# Split the Kafka message values and select the columns
split_data = kafka_source.select(split(col("value"), ",").alias("split_data"))
kafka_df_with_columns = split_data.select(
    col("split_data")[0].alias("tweet_id"),
    col("split_data")[1].alias("username"),
    col("split_data")[2].alias("tweet_text")
)

def write_to_hive(df, epoch_id):
    df.write \
        .mode("append") \
        .format("hive") \
        .saveAsTable(hive_table)

# Apply the write_to_hive function to each micro-batch
kafka_df_with_columns.writeStream \
    .foreachBatch(write_to_hive) \
    .start() \
    .awaitTermination()

spark.stop()
