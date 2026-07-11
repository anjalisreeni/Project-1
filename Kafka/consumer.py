"""
Kafka Consumer
Consumes sensor data from a Kafka topic and forwards it downstream (e.g. Snowflake).
"""
import json
from kafka import KafkaConsumer

KAFKA_BROKER = "localhost:9092"
TOPIC_NAME = "iot-sensor-data"
GROUP_ID = "iot-consumer-group"


def create_consumer() -> KafkaConsumer:
    return KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=[KAFKA_BROKER],
        group_id=GROUP_ID,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    )


def consume_messages():
    consumer = create_consumer()
    print(f"Listening on topic '{TOPIC_NAME}'...")

    for message in consumer:
        data = message.value
        print(f"Received: {data}")
        # TODO: forward `data` to Snowflake or another sink


if __name__ == "__main__":
    consume_messages()
