from kafka import KafkaConsumer
import json


if __name__ == '__main__':

    consumer = KafkaConsumer(
        'Bitcoin',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        # group_id='bitcoin-group',
        api_version=(0, 10, 1)
    )

    print('Start :')
    for msg in consumer:
        print(json.loads(msg.value))