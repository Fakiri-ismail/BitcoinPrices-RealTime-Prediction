import findspark
findspark.init(spark_home='D:\spark')

from pyspark.sql import SparkSession

mongo = SparkSession.builder.appName("BitcoinPrediction") \
    .config("spark.mongodb.input.uri", "mongodb://127.0.0.1:27017/Bitcoin.data") \
    .config("spark.mongodb.output.uri", "mongodb://127.0.0.1:27017/Bitcoin.data") \
    .config('spark.jars.packages', 'org.mongodb.spark:mongo-spark-connector_2.11:2.4.2') \
    .getOrCreate()

df = mongo.read.format("com.mongodb.spark.sql.DefaultSource").load()
df.printSchema()
df.show(truncate=False)