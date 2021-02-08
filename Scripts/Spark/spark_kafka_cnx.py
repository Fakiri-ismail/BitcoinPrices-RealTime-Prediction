import findspark
findspark.init(spark_home='D:\spark')

from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

def getSqlContext(conf):
    input_uri = "mongodb://localhost:27017/Bitcoin.bitcoin"
    output_uri = "mongodb://localhost:27017/Bitcoin.bitcoin"

    conf.set('spark.mongodb.input.uri', input_uri)
    conf.set('spark.mongodb.output.uri', output_uri)
    conf.set('spark.mongodb.input.sampleSize', 50000)

    sc=SparkContext.getOrCreate(conf=conf)
    return SQLContext(sc)


conf = SparkConf().setAppName("BitcoinPrediction").setMaster('local')
sc = SparkContext.getOrCreate(conf=conf)
ssc = StreamingContext(sc, 5)
data = KafkaUtils.createDirectStream(ssc, topics=["Bitcoin"], kafkaParams={"metadata.broker.list":"localhost:9092"})

sqlContext = getSqlContext(conf)

# data.foreachRDD(lambda rdd: rdd.collect().toList)
df = sqlContext.createDataFrame(data.foreachRDD(lambda rdd: rdd.map(lambda x: (x[0], list(set(x[1]))))),"ok")
df.write.format("mongo").mode("append").save()

ssc.start()
ssc.awaitTermination()
