from kafka import KafkaProducer
import urllib.request
import json
import time

# def json_serializer(data):
#     return json.dumps(data).encode('utf-8')

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    # value_serializer=json_serializer,
    api_version=(0, 10, 1)
)

if __name__ == '__main__':
    print("Seending Data >>>>> ")
    while 1:
        url = "https://data.messari.io/api/v1/assets/btc/metrics/market-data"
        bitcoineData = urllib.request.urlopen(url).read()

        print(json.loads(bitcoineData))
        producer.send('Bitcoin',bitcoineData)

        time.sleep(5)