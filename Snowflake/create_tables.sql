-- Create database and schema
CREATE DATABASE IF NOT EXISTS IOT_DB;
USE DATABASE IOT_DB;
CREATE SCHEMA IF NOT EXISTS RAW;
USE SCHEMA RAW;

-- Raw sensor data table
CREATE TABLE IF NOT EXISTS SENSOR_DATA (
    sensor_id     STRING,
    event_timestamp TIMESTAMP_NTZ,
    temperature   FLOAT,
    humidity      FLOAT,
    pressure      FLOAT,
    loaded_at     TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
);

-- Optional staging table for Kafka connector loads
CREATE TABLE IF NOT EXISTS SENSOR_DATA_STAGING (
    record_content VARIANT,
    loaded_at      TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
);
