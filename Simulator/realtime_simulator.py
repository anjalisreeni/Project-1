
import pandas as pd
import random
import time
from datetime import datetime
import warnings

warnings.filterwarnings("ignore")

# Read dataset
df = pd.read_csv("../Data/sensor_data.csv")

def generate_sensor_data():

    for index, row in df.head(500).iterrows():

        sensor_data = row.to_dict()

        # Update timestamp
        sensor_data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Temperature changes slightly
        sensor_data["temperature"] = round(sensor_data["temperature"] + random.uniform(-0.3, 0.3), 2)

        # Humidity changes slightly
        sensor_data["humidity"] = round(sensor_data["humidity"] + random.uniform(-2, 2), 2)

        # Vibration changes slightly
        sensor_data["vibration"] = round(sensor_data["vibration"] + random.uniform(-0.2, 0.2), 2)

        # Battery slowly drains
        sensor_data["battery_level"] = max(0, sensor_data["battery_level"] - random.randint(0, 1))

        # Calculate Risk Score
        risk_score = 0

        if sensor_data["temperature"] > 7:
            risk_score += 30

        if sensor_data["battery_level"] < 75:
            risk_score += 20

        if sensor_data["door_status"] == "Open":
            risk_score += 25

        if sensor_data["vibration"] > 4:
            risk_score += 25

        sensor_data["risk_score"] = risk_score

        # Alert Status
        if risk_score >= 70:
            sensor_data["alert_status"] = "Critical"
        elif risk_score >= 40:
            sensor_data["alert_status"] = "Warning"
        else:
            sensor_data["alert_status"] = "Normal"

        yield sensor_data
        time.sleep(1)


if __name__ == "__main__":
    for sensor_data in generate_sensor_data():
        print("=" * 70)
        print(sensor_data)