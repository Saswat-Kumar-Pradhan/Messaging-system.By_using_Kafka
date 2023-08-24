from kafka import KafkaProducer
import json
from data import get_registered_user
import time

producer = KafkaProducer(bootstrap_servers='localhost:29092')
topic = "firsttopic"
for i in range(10):
    x = input("Write something here :")
    data={"msg": x}
    producer.send("firsttopic",json.dumps(data).encode("utf-8"))
    print("sent")
    time.sleep(1)











# if __name__ == "__main__":
#     while True:
#         registered_user = get_registered_user()
#         print(registered_user)
#         producer.send("mytopic",registered_user)
#         time.sleep(3)
