# Real-time Sentiment Analysis

## Tools Used
### Operating System
- Ubuntu
  
### Programming Languages
- Python
- Java
- JavaScript

### Big Data Tools
- Spark
- Kafka
- Hadoop

### Software Frameworks
- Flask
- Spring Boot

## Spark Execution Mode : Local

## Project Architecture

![ProjectArchitecture](https://github.com/AshikJenly/REAL_TIME_SENTIMENT_ANALYSIS/assets/116492348/2e4587e3-5c01-4d3a-9a43-6cfd02dad975)


# How to Execute the Project
## Step 1: Starting All the Required Processes (Background/Foreground)



1. Start Hadoop:
   ```bash
   $ /path/to/hadoop/sbin/start-all.sh
   ```

2. Start Spark:
   ```bash
   $ /path/to/spark/sbin/start-all.sh
   ```

3. Start Kafka:

   - Start Zookeeper:
     ```bash
     $ sudo /path/to/kafka/bin/zookeeper-server-start.sh config/zookeeper.properties
     ```

   - Start Kafka:
     ```bash
     $ sudo /path/to/kafka/bin/kafka-server-start.sh config/server.properties
     ```

   - Create a topic in Kafka:
     ```bash
     $ /path/to/kafka/bin/kafka-topics.sh --create --topic tweets --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
     ```

   Processes up and running:

   - Hadoop:
     - ResourceManager
     - NodeManager
     - DataNode
     - SecondaryNameNode

   - Spark:
     - Worker
     - Master

   - Kafka:
     - Zookeeper
     - Kafka
     - Jps

## Step 2: Submitting Spark Jobs

1. Job to Store Data from Kafka to HDFS in Stream:
   ```bash
   $ spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 StoringDataInStream/DataSource.py
   ```

2. Job to Read Data in Stream from HDFS and Provide an API:
   ```bash
   $ spark-submit RetrievingDataInStream/main.py
   ```

## Step 3: Run the User Interface of Twitter

- Option 1: Using Maven in UserInterface/mvnw:
  ```bash
  $ cd UserInterface
  $ ./mvnw spring-boot:run
  ```

- Option 2: Using an IDE

## Step 4: Open Visualization UI

- In your web browser, access the following path:
  ```
  /path/to/VisualizationUI/index.html
  ```

**Make sure to replace `/path/to` with the actual path to your project files and executables.**



# Output Sample:

![Screenshot from 2023-10-05 21-09-17](https://github.com/AshikJenly/REAL_TIME_SENTIMENT_ANALYSIS/assets/116492348/5c9cc4ee-eb45-4661-abec-f90dad3a9717)


![Screenshot from 2023-10-05 21-38-32](https://github.com/AshikJenly/REAL_TIME_SENTIMENT_ANALYSIS/assets/116492348/9bb3937d-28cb-4622-bd93-26b1d8c6adc4)

