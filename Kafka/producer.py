import pandas as pd
import time
import json
import os
from datetime import datetime
from kafka import KafkaProducer
import warnings

from risk_utils import process_reading

warnings.filterwarnings("ignore")

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic_name = 'container_sensor_data'
print("Connected to Kafka")
print("Sending Data...")

# --- Load data ---
csv_path = "Data/sensor_data.csv"
print(f"Looking for data at exactly this location: {os.path.abspath(csv_path)}")

try:
    df = pd.read_csv(csv_path)

    # Normalize column names: strip whitespace, lowercase, spaces -> underscores
    df.columns = (
        df.columns.str.strip()
                  .str.lower()
                  .str.replace(" ", "_")
    )

    print(f"Success! Found {len(df)} rows of data.")
    print(f"Columns detected: {list(df.columns)}")

    required_cols = {"vibration", "battery_level", "temperature", "door_status"}
    missing = required_cols - set(df.columns)
    if missing:
        print(f"ERROR: CSV is missing expected column(s): {missing}")
        print("Check for typos, extra spaces, or different capitalization in the CSV header.")
        exit()

    if len(df) == 0:
        print("ERROR: The CSV file is empty! You need to run your iot_simulator.py first to generate data.")
        exit()

except FileNotFoundError:
    print(f"ERROR: Could not find the file at {os.path.abspath(csv_path)}. Please check your folder structure!")
    exit()
# -----------------------------

# Stream data continuously
for index, row in df.iterrows():
    sensor_data = row.to_dict()
    sensor_data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Apply drift + compute risk_score / alert_status (shared logic)
    sensor_data = process_reading(sensor_data)

    # Send the simulated live data to the Kafka topic
    producer.send(topic_name, sensor_data)

    print("=" * 50)
    print("Message Sent")
    print(f"Container ID: {sensor_data['container_id']} | Risk: {sensor_data['risk_score']} | Status: {sensor_data['alert_status']}")
    print(f"Full record ({len(sensor_data)} fields): {sensor_data}")

    # Wait 1 second before generating the next reading
    time.sleep(1)

producer.flush()
print("All records sent.")