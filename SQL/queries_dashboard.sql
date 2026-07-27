CREATE DATABASE atmosync;
USE atmosync;
SELECT * FROM sensor_data_feature_engineered LIMIT 5;
-- Total Shipments
SELECT COUNT(DISTINCT shipment_id) AS total_shipments
FROM sensor_data_feature_engineered;

-- Total Container
SELECT COUNT(DISTINCT container_id) AS total_containers
FROM sensor_data_feature_engineered;

-- Average Temperature, Humidity and Battery
SELECT
ROUND(AVG(temperature),2) AS avg_temperature,
ROUND(AVG(humidity),2) AS avg_humidity,
ROUND(AVG(battery_level),2) AS avg_battery
FROM sensor_data_feature_engineered;

-- Shipment Status Distribution
SELECT
container_status,
COUNT(*) AS total
FROM sensor_data_feature_engineered
GROUP BY container_status
ORDER BY total DESC;

-- Shipments by Fruit Type
SELECT
fruit_type,
COUNT(*) AS total_shipments
FROM sensor_data_feature_engineered
GROUP BY fruit_type
ORDER BY total_shipments DESC;

-- Average Temperature by Fruit Type
SELECT
fruit_type,
ROUND(AVG(temperature),2) AS avg_temperature
FROM sensor_data_feature_engineered
GROUP BY fruit_type
ORDER BY avg_temperature DESC;

-- Top 5 Highest Temperature Readings
SELECT
container_id,
temperature,
timestamp
FROM sensor_data_feature_engineered
ORDER BY temperature DESC
LIMIT 5;

-- High Risk Containers
SELECT
container_id,
shipment_id,
risk_level
FROM sensor_data_feature_engineered
WHERE risk_level='High';

-- Battery Status Distribution
SELECT
battery_status,
COUNT(*) AS total
FROM sensor_data_feature_engineered
GROUP BY battery_status;

-- Average Temperature by Route
SELECT
route,
ROUND(AVG(temperature),2) AS avg_temperature
FROM sensor_data_feature_engineered
GROUP BY route
ORDER BY avg_temperature DESC;

-- Origin-wise Shipments
SELECT
origin,
COUNT(*) AS total_shipments
FROM sensor_data_feature_engineered
GROUP BY origin
ORDER BY total_shipments DESC;

-- Destination-wise Shipments
SELECT
destination,
COUNT(*) AS total_shipments
FROM sensor_data_feature_engineered
GROUP BY destination
ORDER BY total_shipments DESC;

-- Hourly Sensor Readings
SELECT
hour,
COUNT(*) AS total_readings
FROM sensor_data_feature_engineered
GROUP BY hour
ORDER BY hour;

-- Containers with Low Battery
SELECT
container_id,
battery_level
FROM sensor_data_feature_engineered
WHERE battery_level < 20;

-- Temperature Status Distribution
SELECT
temperature_status,
COUNT(*) AS total
FROM sensor_data_feature_engineered
GROUP BY temperature_status;