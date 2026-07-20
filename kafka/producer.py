import os
import sys
import json
from kafka import KafkaProducer

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from iot_simulator import get_sensor_data

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

topic = "container_sensor_data"

print("Producer started...\n")

for sensor in get_sensor_data():
    producer.send(topic, sensor)
    producer.flush()
    print("Sent:", sensor)