from pyspark.sql import SparkSession
from flask import Flask, request, jsonify
import threading
app = Flask(__name__)
DATAFRAME = None


def run_spark_streaming():
    spark = SparkSession.builder\
        .appName("Streaming")\
            .config("spark.sql.streaming.schemaInference", "true")\
                .getOrCreate()

    input_path = "hdfs:///user/stream/tweet"
    streaming = spark.readStream \
        .format("csv") \
        .option("header", "true") \
        .option("maxFilesPerTrigger",1) \
        .load(input_path)

        
    activityCounts = streaming.groupBy("author").count()


    spark.conf.set("spark.sql.shuffle.partitions", 5) 


    def getBatchProcess(batch_df):
        global DATAFRAME
        counts = batch_df.groupBy("author").count()
        count_df_pandas = counts.toPandas()
        # dataFrame =  count_df_pandas
        print(count_df_pandas)
        DATAFRAME = count_df_pandas

    query = activityCounts.writeStream \
        .outputMode("complete")\
            .format("console")\
                .foreachBatch(lambda batch_df,batch_id:getBatchProcess(batch_df))\
                    .queryName("myQuery")\
                        .start()
    query.awaitTermination()



@app.route('/api/stream', methods=['GET'])
def start_streaming():
    
    if DATAFRAME is not None:
        return DATAFRAME.to_json()
    else:
        return jsonify({"message ":"none"})

def threaded_job():
    run_spark_streaming()
    
if __name__ == '__main__':
    thread = threading.Thread(target=threaded_job)
    thread.start()
    app.run(host='0.0.0.0', port=5000)
    thread.join()
