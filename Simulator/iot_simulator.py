
import pandas as pd
import random
import time
import os
from datetime import datetime

# Create Data folder if it doesn't exist
os.makedirs("Data", exist_ok=True)
# CSV file path
file_path = "Data/sensor_data.csv"


# List of container IDs
containers = ["C001", "C002", "C003", "C004", "C005"]

print("IoT Simulator Started...")
print("Press Ctrl + C to stop.\n")

while True:
    # Generate one sensor reading
    data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "container_id": random.choice(containers),
        "temperature": round(random.uniform(2, 10), 2),   # °C
        "humidity": round(random.uniform(70, 95), 2),      # %
        "vibration": round(random.uniform(0, 5), 2),       # vibration level
        "latitude": round(random.uniform(18.90, 19.30), 6),
        "longitude": round(random.uniform(72.70, 73.10), 6)
    }

    # Convert to DataFrame
    df = pd.DataFrame([data])

    # Save to CSV
    if not os.path.exists(file_path):
        df.to_csv(file_path, index=False)
    else:
        df.to_csv(file_path, mode="a", header=False, index=False)

    # Print the generated data
    print(data)

    # Wait for 1 second before generating the next reading
    time.sleep(1)