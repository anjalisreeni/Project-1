
import pandas as pd
import snowflake.connector
import time
import random
from datetime import datetime

print("Streaming script started...")

# Connect to Snowflake
conn = snowflake.connector.connect(
    account="MY_ACCOUNT",
    user="MY_USERNAME",
    password="MY_PASSWORD",
    role="ACCOUNTADMIN",
    warehouse="ATMOSYNC_WH",
    database="ATMOSYNC_DB",
    schema="RAW"
)

cursor = conn.cursor()

# Read dataset once
df = pd.read_csv(
    r"C:\Users\sayam\Desktop\Atmosync\Project-1\Data\sensor_data_feature_engineered.csv"
)

print(f"Loaded {len(df)} rows.")

while True:

    # Pick a random container from the dataset
    row = df.sample(1).iloc[0]

    # Simulate live sensor readings
    temperature = round(float(row["temperature"]) + random.uniform(-2.5, 2.5), 2)
    humidity = round(float(row["humidity"]) + random.uniform(-5, 5), 2)
    vibration = round(max(0, float(row["vibration"]) + random.uniform(-0.8, 0.8)), 2)
    battery = max(5, int(row["battery_level"]) - random.randint(0, 2))

    # NEW timestamp every insert
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Update statuses
    if temperature > 8:
        temp_status = "High"
        risk = "Critical"
        container_status = "At Risk"
    elif temperature > 5:
        temp_status = "Warning"
        risk = "Warning"
        container_status = "Monitoring"
    else:
        temp_status = "Normal"
        risk = "Safe"
        container_status = "Healthy"

    battery_status = "Low" if battery < 30 else "Good"

    cursor.execute("""
        INSERT INTO CONTAINER_SENSOR_DATA
        (
            CONTAINER_ID,
            SHIPMENT_ID,
            FRUIT_TYPE,
            ORIGIN,
            DESTINATION,
            TEMPERATURE,
            HUMIDITY,
            VIBRATION,
            BATTERY_LEVEL,
            DOOR_STATUS,
            CONTAINER_STATUS,
            LATITUDE,
            LONGITUDE,
            TIMESTAMP,
            RISK_LEVEL,
            BATTERY_STATUS,
            TEMPERATURE_STATUS,
            DATE,
            HOUR,
            ROUTE
        )
        VALUES
        (
            %s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s
        )
    """, (
        row["container_id"],
        row["shipment_id"],
        row["fruit_type"],
        row["origin"],
        row["destination"],
        temperature,
        humidity,
        vibration,
        battery,
        row["door_status"],
        container_status,
        float(row["latitude"]),
        float(row["longitude"]),
        timestamp,
        risk,
        battery_status,
        temp_status,
        datetime.now().date(),
        datetime.now().hour,
        row["route"]
    ))

    conn.commit()

    print(
        f"{timestamp} | {row['container_id']} | "
        f"Temp={temperature}°C | Risk={risk}"
    )

    # Insert one row every 3 seconds
    time.sleep(3)