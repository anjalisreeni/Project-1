import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "container_sensor_data",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("Consumer started...\n")

for message in consumer:

    print("Received:", message.value)