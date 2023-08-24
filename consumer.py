from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
                        "firsttopic",
                        bootstrap_servers='localhost:29092'
                        # auto_offset_reset='earliest',
                        # group_id="c_group_01"
                        )
print("starting the consumer")
for msg in consumer:
    print(json.loads(msg.value))
    # print(msg.value)
