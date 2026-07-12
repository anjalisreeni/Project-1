"""
IoT Sensor Data Simulator
Generates synthetic sensor readings and writes them to CSV / streams them to Kafka.
"""
import csv
import random
import time
from datetime import datetime, timezone

SENSOR_IDS = [f"sensor_{i:03d}" for i in range(1, 11)]
OUTPUT_CSV = "Data/sensor_data.csv"


def generate_reading(sensor_id: str) -> dict:
    return {
        "sensor_id": sensor_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "temperature": round(random.uniform(15.0, 35.0), 2),
        "humidity": round(random.uniform(20.0, 80.0), 2),
        "pressure": round(random.uniform(980.0, 1050.0), 2),
    }


def run_simulation(interval_seconds: float = 1.0, iterations: int = 100):
    fieldnames = ["sensor_id", "timestamp", "temperature", "humidity", "pressure"]

    with open(OUTPUT_CSV, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if f.tell() == 0:
            writer.writeheader()

        for _ in range(iterations):
            sensor_id = random.choice(SENSOR_IDS)
            reading = generate_reading(sensor_id)
            writer.writerow(reading)
            f.flush()
            print(reading)
            time.sleep(interval_seconds)


if __name__ == "__main__":
    run_simulation()
