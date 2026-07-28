import random
import time
import snowflake.connector

conn = snowflake.connector.connect(
    user="JIYAPENDHARI",
    password="JiyaPendhari20",
    account="LRNCIIW-AY84983",
    warehouse="ATMOSYNC_WH",
    database="ATMOSYNC_DB",
    schema="RAW"
)

cursor = conn.cursor()

sensor_id = 2

while True:

    temperature = round(random.uniform(20, 35), 2)
    humidity = random.randint(40, 90)
    pressure = random.randint(1000, 1025)
    co2 = random.randint(350, 600)
    pm25 = round(random.uniform(5, 30), 2)
    pm10 = round(random.uniform(10, 50), 2)

    daytime = "DAY"

    cursor.execute("""
    INSERT INTO CONTAINER_SENSOR_DATA
    (
        ID,
        TIMESTAMP,
        TEMPERATURE,
        HUMIDITY,
        PRESSURE,
        CO2_GAS,
        PM2_5,
        PM10,
        DAYTIME
    )
    VALUES
    (%s,CURRENT_TIMESTAMP(),%s,%s,%s,%s,%s,%s,%s)
    """,
    (
        sensor_id,
        temperature,
        humidity,
        pressure,
        co2,
        pm25,
        pm10,
        daytime
    ))

    conn.commit()

    print("Inserted:", sensor_id, temperature)

    sensor_id += 1

    time.sleep(5)