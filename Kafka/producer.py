"""
Kafka Producer
Reads sensor data and publishes it to a Kafka topic.
"""
import json
import time
from kafka import KafkaProducer

KAFKA_BROKER = "localhost:9092"
TOPIC_NAME = "iot-sensor-data"


def create_producer() -> KafkaProducer:
    return KafkaProducer(
        bootstrap_servers=[KAFKA_BROKER],
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )


def send_message(producer: KafkaProducer, message: dict):
    producer.send(TOPIC_NAME, value=message)
    producer.flush()
    print(f"Sent: {message}")


if __name__ == "__main__":
    producer = create_producer()

    # Example: send a test message
    sample_message = {
        "sensor_id": "sensor_001",
        "temperature": 22.5,
        "humidity": 45.0,
        "pressure": 1013.25,
        "timestamp": time.time(),
    }
    send_message(producer, sample_message)
