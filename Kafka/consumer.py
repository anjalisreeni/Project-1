"""
consumer.py

Reads container sensor readings from the 'container_sensor_data' Kafka
topic (published by producer.py) and prints them out, highlighting any
Warning/Critical alerts.

Expected message schema (16 fields), matching producer.py:
container_id, shipment_id, fruit_type, origin, destination,
temperature, humidity, vibration, battery_level, door_status,
container_status, latitude, longitude, timestamp,
risk_score, alert_status
"""

import json
from kafka import KafkaConsumer

TOPIC_NAME = "container_sensor_data"

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=["localhost:9092"],
    auto_offset_reset="earliest",       # read from the beginning of the topic
    enable_auto_commit=True,
    group_id="container_monitor_group",  # consumer group, tracks read offset
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
)

print(f"Connected to Kafka. Listening on topic: {TOPIC_NAME}")
print("Waiting for messages... (Ctrl+C to stop)\n")

try:
    for message in consumer:
        data = message.value

        # Sanity check: confirm we got the full 16-field schema
        expected_fields = {
            "container_id", "shipment_id", "fruit_type", "origin", "destination",
            "temperature", "humidity", "vibration", "battery_level", "door_status",
            "container_status", "latitude", "longitude", "timestamp",
            "risk_score", "alert_status",
        }
        missing = expected_fields - set(data.keys())
        if missing:
            print(f"WARNING: message missing fields {missing}, skipping full print")
            continue

        alert = data["alert_status"]
        marker = "🔴" if alert == "Critical" else "🟡" if alert == "Warning" else "🟢"

        print("=" * 60)
        print(f"{marker} Container {data['container_id']} | Shipment {data['shipment_id']} | {data['fruit_type']}")
        print(f"   Route: {data['origin']} -> {data['destination']}")
        print(f"   Temp: {data['temperature']}°C | Humidity: {data['humidity']}% | Vibration: {data['vibration']}")
        print(f"   Battery: {data['battery_level']}% | Door: {data['door_status']} | Status: {data['container_status']}")
        print(f"   Location: ({data['latitude']}, {data['longitude']})")
        print(f"   Risk Score: {data['risk_score']} | Alert: {alert}")
        print(f"   Timestamp: {data['timestamp']}")

        if alert in ("Warning", "Critical"):
            print(f"   !! ALERT: Container {data['container_id']} needs attention !!")

except KeyboardInterrupt:
    print("\nStopped listening.")
finally:
    consumer.close()
    print("Consumer connection closed.")