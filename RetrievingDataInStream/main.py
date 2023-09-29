from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from flask import Flask, request, jsonify
from flask_cors import CORS
import threading
app = Flask(__name__)
DATAFRAME = None
TWEETS_DATAFRAME = None
CORS(app)
CORS(app, origins=['*'])

custom_schema = StructType([
    StructField("tweet_id", StringType(), True),
    StructField("username", StringType(), True),
    StructField("tweet_data", StringType(), True),
    StructField("sentiment", StringType(), True)
    
])

def run_spark_streaming():
    spark = SparkSession.builder\
        .appName("Streaming")\
            .config("spark.sql.streaming.schemaInference", "true")\
                .getOrCreate()

    input_path = "hdfs:///jenly/projects/sentimentAnalysis/tweets"
    streaming = spark.readStream \
        .format("csv") \
        .schema(custom_schema) \
        .option("header", "false") \
        .option("inferSchema","false") \
        .option("maxFilesPerTrigger",1) \
        .load(input_path)

    
    activityCounts = streaming.groupBy("sentiment").count()


    spark.conf.set("spark.sql.shuffle.partitions", 5) 


    def getBatchProcess(batch_df):
       
        global DATAFRAME
        count_df_pandas = batch_df.toPandas()
        
        print(count_df_pandas)
        DATAFRAME = count_df_pandas

    query = activityCounts.writeStream \
        .outputMode("complete")\
            .format("console")\
                .foreachBatch(lambda batch_df,batch_id:getBatchProcess(batch_df))\
                    .queryName("myQuery")\
                        .start()
    query.awaitTermination()


spark_batch = SparkSession.builder\
        .appName("Get Tweets")\
                .getOrCreate()

def run_spark_batch():
    """Returns all the tweets"""
    input_path = "hdfs:///jenly/projects/sentimentAnalysis/tweets"
    data = spark_batch.read\
        .csv(input_path,schema=custom_schema)

    return data.toPandas()
    





@app.route('/api/stream', methods=['GET'])
def start_streaming():
    
    if DATAFRAME is not None:
        return DATAFRAME.to_json()
    else:
        return jsonify({"message ":"none"})



@app.route('/api/getalltweets',methods=["GET"])
def get_tweets():
    global TWEETS_DATAFRAME
    if TWEETS_DATAFRAME is not None:
        return TWEETS_DATAFRAME.to_json()
    else:
        TWEETS_DATAFRAME = run_spark_batch()
        return jsonify({"message ":"none"})

def threaded_job():
    run_spark_streaming()
    
if __name__ == '__main__':
    thread = threading.Thread(target=threaded_job)
    thread.start()
    app.run(host='0.0.0.0', port=5000)
    thread.join()
