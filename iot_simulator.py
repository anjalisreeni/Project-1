import pandas as pd
import time
from datetime import datetime

# Read dataset
data = pd.read_csv("data/dataset.csv")

def get_sensor_data():
    """
    Reads one row from the dataset every second
    and returns it as a Python dictionary.
    """

    while True:   # Keep streaming forever

        for _, row in data.iterrows():

            sensor_data = {
                "id": int(row["ID"]),

                # Current system time
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

                "temperature": float(row["Temperature"]),
                "humidity": float(row["Humidity"]),
                "pressure": float(row["Pressure"]),
                "co2_gas": int(row["Co2 Gas"]),
                "pm2_5": float(row["PM2.5"]),
                "pm10": float(row["PM10"]),
                "daytime": row["Daytime"]
            }

            yield sensor_data

            time.sleep(1)


# Test the simulator
if __name__ == "__main__":

    print("Starting Real-Time IoT Simulator...\n")

    for sensor in get_sensor_data():
        print(sensor)