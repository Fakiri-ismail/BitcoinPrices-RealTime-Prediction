from kafka import KafkaConsumer
from pymongo import MongoClient
import json
import datetime

consumer = KafkaConsumer(
        'Bitcoin',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        # group_id='bitcoin-group',
        api_version=(0, 10, 1)
    )

client = MongoClient('localhost', 27017)
db = client['Bitcoin']
collection = db['data']

print(">>>> Receiving Data ...")
for msg in consumer:
    my_json = msg.value.decode('utf8').replace("'", '"')
    data = json.loads(my_json)
    s = json.dumps(data, indent=4, sort_keys=True)

    timestamp = {"timestamp": datetime.datetime.strptime(data["status"]["timestamp"][:-4], '%Y-%m-%dT%H:%M:%S.%f')}
    price = {"price_usd": data["data"]["market_data"]["price_usd"]}
    data_cleaned = timestamp.copy()
    data_cleaned.update(price)

    print("Sending it to mongoDb >>>")
    print("data_cleaned : ", data_cleaned)
    collection.insert_one(data_cleaned)
    print("- - -" * 5)