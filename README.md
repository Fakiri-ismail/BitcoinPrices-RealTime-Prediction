# Bitcoin Prices Prediction in Real-Time
Authors : DRIOUCHE Adnane, FAKIRI Ismail, EL AMRANI EL IDRISSI Oumaima et OUAZIZ Hajar

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## I. Description
This project will allow you to predict the price of bitoin in real time using Kafka, Spark and MongoDb as a database.<br/>
This is the architecture of the App : 
![project_Big_Data](https://user-images.githubusercontent.com/46791116/105404886-c812f700-5c2a-11eb-8c8d-4affe90e9d58.png)
>>We are using the [Messari's API](https://messari.io/api/docs#operation/Get%20all%20Assets) to collect data in real-time. 

Description of files : 
- producer.py : this is a python script that create our own Kafka Producer.
- kafka_mongo.py : this is our Consumer that get data from the producer and stock them on MongoDB
- Mongo_Spark_LSTM.ipynb : this file content is a script of our model LSTM that starts automatically every hour


## II. Installation 
First, you have to install Spark and Kafka.
To install Kafka for : 
- Windows 10 : see this [link](https://www.goavega.com/install-apache-kafka-on-windows/)
- Ubuntu 16.04 & 18.04 : see this [link](https://tecadmin.net/install-apache-kafka-ubuntu/)

To install Spark : 
- Windows 10 : see this [link](https://phoenixnap.com/kb/install-spark-on-windows-10)
- Ubuntu 16.04 & 18.04 : see this [link](https://computingforgeeks.com/how-to-install-apache-spark-on-ubuntu-debian/)

Then install the dependencies and devDependencies.

```sh
$ pip install requirements.txt
```
## III. Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
## IV. Licence
**This is a Free project !**
**Feel Free and clone it :)**
