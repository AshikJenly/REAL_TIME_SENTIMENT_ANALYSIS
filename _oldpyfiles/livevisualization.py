from pyspark.sql import SparkSession
from pyspark.sql.functions import split, col,udf,concat_ws
from pyspark.sql.types import StringType


spark = SparkSession.builder \
    .appName("SparkStreaming Visualization") \
    .enableHiveSupport() \
    .getOrCreate()
spark.sparkContext.setLogLevel("DEBUG")
spark.conf.set("spark.sql.shuffle.partitions", 5) #To avoid to much partitions

streaming_data = spark.readStream \
    .table("stmtdata.datatweet") \
    .select("sentiment")
    
    
categories = []
counts = []
def process_batch(batch_df):
    global categories,counts
    
    categories = batch_df.select("sentiment").rdd.flatMap(lambda x: x).collect()
    counts = batch_df.select("count").rdd.flatMap(lambda x: x).collect()

query = streaming_data\
    .groupBy("sentiment")\
        .count().alias("count")\
            .writeStream.outputMode("complete")\
                .foreachBatch(lambda batch_df, batch_id: process_batch(batch_df))\
                    .start()\
                        .awaitTermination()
                        
print(categories)
print(counts)
spark.stop()
                
