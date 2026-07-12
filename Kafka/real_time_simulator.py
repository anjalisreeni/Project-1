"""
real_time_simulator.py

Generates simulated container cold-chain sensor readings and writes
them to Data/sensor_data.csv in the schema producer.py expects:

container_id, shipment_id, fruit_type, origin, destination,
temperature, humidity, vibration, battery_level, door_status,
container_status, latitude, longitude, timestamp

This REPLACES the old real_time_simulator.py, which was accidentally
saved as raw notebook JSON instead of executable Python (that's why
running it did nothing).
"""

import csv
import random
from datetime import datetime, timezone

from risk_utils import apply_drift  # reuse the same drift logic as producer.py

OUTPUT_CSV = "Data/sensor_data.csv"

FRUITS = ["Grapes", "Mango", "Apple", "Banana", "Papaya", "Pineapple", "Kiwi", "Orange", "Strawberry", "Pomegranate"]
CITIES = ["Ahmedabad", "Delhi", "Mumbai", "Hyderabad", "Kolkata", "Pune", "Bangalore", "Chennai"]
DOOR_STATUSES = ["Closed", "Open"]
CONTAINER_STATUSES = ["In Transit", "Delivered", "Loading", "Unloading"]

# Rough lat/lon anchors per city so points look geographically plausible
CITY_COORDS = {
    "Ahmedabad": (23.02, 72.57),
    "Delhi": (28.61, 77.20),
    "Mumbai": (19.07, 72.87),
    "Hyderabad": (17.38, 78.48),
    "Kolkata": (22.57, 88.36),
    "Pune": (18.52, 73.85),
    "Bangalore": (12.97, 77.59),
    "Chennai": (13.08, 80.27),
}

FIELDNAMES = [
    "container_id", "shipment_id", "fruit_type", "origin", "destination",
    "temperature", "humidity", "vibration", "battery_level", "door_status",
    "container_status", "latitude", "longitude", "timestamp",
]


def generate_container_reading(container_num: int) -> dict:
    origin = random.choice(CITIES)
    destination = random.choice([c for c in CITIES if c != origin])
    lat, lon = CITY_COORDS[origin]

    reading = {
        "container_id": f"C{container_num:03d}",
        "shipment_id": f"S{random.randint(0, 999):05d}",
        "fruit_type": random.choice(FRUITS),
        "origin": origin,
        "destination": destination,
        "temperature": round(random.uniform(1.5, 8.0), 2),
        "humidity": round(random.uniform(70.0, 95.0), 2),
        "vibration": round(random.uniform(0.0, 5.0), 2),
        "battery_level": random.randint(70, 100),
        "door_status": random.choices(DOOR_STATUSES, weights=[90, 10])[0],
        "container_status": random.choice(CONTAINER_STATUSES),
        "latitude": round(lat + random.uniform(-0.05, 0.05), 6),
        "longitude": round(lon + random.uniform(-0.05, 0.05), 6),
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
    }
    return reading


def run_simulation(num_containers: int = 100):
    with open(OUTPUT_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()

        for i in range(1, num_containers + 1):
            reading = generate_container_reading(i)
            writer.writerow(reading)

    print(f"Wrote {num_containers} rows to {OUTPUT_CSV}")


if __name__ == "__main__":
    run_simulation(num_containers=300)