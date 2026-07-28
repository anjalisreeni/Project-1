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
(
    1,
    CURRENT_TIMESTAMP(),
    27.5,
    65,
    1012,
    420,
    18.5,
    32.1,
    'DAY'
)
""")

conn.commit()

print("✅ Data Inserted Successfully!")

cursor.close()
conn.close()