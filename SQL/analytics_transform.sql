USE DATABASE ATMOSYNC_DB;

CREATE SCHEMA IF NOT EXISTS ANALYTICS;

USE SCHEMA ANALYTICS;

-- =====================================================
-- Create Analytics Table
-- =====================================================

CREATE OR REPLACE TABLE CONTAINER_ANALYTICS (

    CONTAINER_ID VARCHAR,
    SHIPMENT_ID VARCHAR,
    FRUIT_TYPE VARCHAR,
    ORIGIN VARCHAR,
    DESTINATION VARCHAR,

    TEMPERATURE FLOAT,
    HUMIDITY FLOAT,
    VIBRATION FLOAT,
    BATTERY_LEVEL NUMBER,

    RISK_SCORE NUMBER(5,2),
    SPOILAGE_RISK VARCHAR,
    TIME_TO_SPOILAGE NUMBER(5,2),

    ESTIMATED_LOSS NUMBER(10,2),
    RECOMMENDED_MARKET VARCHAR,
    ARBITRAGE_PROFIT NUMBER(10,2),

    RECOMMENDED_ACTION VARCHAR,

    TIMESTAMP TIMESTAMP_NTZ
);

-- =====================================================
-- Initial Analytics Load
-- =====================================================

INSERT INTO ANALYTICS.CONTAINER_ANALYTICS

SELECT

    CONTAINER_ID,
    SHIPMENT_ID,
    FRUIT_TYPE,
    ORIGIN,
    DESTINATION,

    TEMPERATURE,
    HUMIDITY,
    VIBRATION,
    BATTERY_LEVEL,

    (
        CASE
            WHEN TEMPERATURE <= 5 THEN 10
            WHEN TEMPERATURE <= 8 THEN 20
            ELSE 35
        END +

        CASE
            WHEN HUMIDITY <= 70 THEN 10
            WHEN HUMIDITY <= 85 THEN 20
            ELSE 30
        END +

        CASE
            WHEN VIBRATION <= 2 THEN 5
            WHEN VIBRATION <= 4 THEN 10
            ELSE 15
        END +

        CASE
            WHEN BATTERY_LEVEL >= 80 THEN 5
            WHEN BATTERY_LEVEL >= 50 THEN 10
            ELSE 20
        END

    ) AS RISK_SCORE,

    CASE
        WHEN TEMPERATURE > 8 OR HUMIDITY > 85 THEN 'Critical'
        WHEN TEMPERATURE > 5 OR HUMIDITY > 75 THEN 'Warning'
        ELSE 'Safe'
    END AS SPOILAGE_RISK,

    CASE
        WHEN TEMPERATURE > 8 THEN 8
        WHEN TEMPERATURE > 5 THEN 24
        ELSE 72
    END AS TIME_TO_SPOILAGE,

    CASE
        WHEN TEMPERATURE > 8 THEN 2500
        WHEN TEMPERATURE > 5 THEN 1200
        ELSE 300
    END AS ESTIMATED_LOSS,

    CASE
        WHEN TEMPERATURE > 8 THEN 'Nearest Local Market'
        WHEN TEMPERATURE > 5 THEN 'Regional Distribution Center'
        ELSE 'Primary Export Market'
    END AS RECOMMENDED_MARKET,

    CASE
        WHEN TEMPERATURE > 8 THEN 1500
        WHEN TEMPERATURE > 5 THEN 3200
        ELSE 4700
    END AS ARBITRAGE_PROFIT,

    CASE
        WHEN TEMPERATURE > 8 THEN 'Immediate Reroute'
        WHEN TEMPERATURE > 5 THEN 'Monitor Every Hour'
        ELSE 'Continue Standard Route'
    END AS RECOMMENDED_ACTION,

    TIMESTAMP

FROM RAW.CONTAINER_SENSOR_DATA;

-- =====================================================
-- Automated Analytics Update Task
-- =====================================================

CREATE OR REPLACE TASK UPDATE_ANALYTICS
WAREHOUSE = COMPUTE_WH
SCHEDULE = '1 MINUTE'
AS

INSERT INTO ANALYTICS.CONTAINER_ANALYTICS

SELECT

    CONTAINER_ID,
    SHIPMENT_ID,
    FRUIT_TYPE,
    ORIGIN,
    DESTINATION,

    TEMPERATURE,
    HUMIDITY,
    VIBRATION,
    BATTERY_LEVEL,

    (
        CASE
            WHEN TEMPERATURE <= 5 THEN 10
            WHEN TEMPERATURE <= 8 THEN 20
            ELSE 35
        END +

        CASE
            WHEN HUMIDITY <= 70 THEN 10
            WHEN HUMIDITY <= 85 THEN 20
            ELSE 30
        END +

        CASE
            WHEN VIBRATION <= 2 THEN 5
            WHEN VIBRATION <= 4 THEN 10
            ELSE 15
        END +

        CASE
            WHEN BATTERY_LEVEL >= 80 THEN 5
            WHEN BATTERY_LEVEL >= 50 THEN 10
            ELSE 20
        END
    ),

    CASE
        WHEN TEMPERATURE > 8 OR HUMIDITY > 85 THEN 'Critical'
        WHEN TEMPERATURE > 5 OR HUMIDITY > 75 THEN 'Warning'
        ELSE 'Safe'
    END,

    CASE
        WHEN TEMPERATURE > 8 THEN 8
        WHEN TEMPERATURE > 5 THEN 24
        ELSE 72
    END,

    CASE
        WHEN TEMPERATURE > 8 THEN 2500
        WHEN TEMPERATURE > 5 THEN 1200
        ELSE 300
    END,

    CASE
        WHEN TEMPERATURE > 8 THEN 'Nearest Local Market'
        WHEN TEMPERATURE > 5 THEN 'Regional Distribution Center'
        ELSE 'Primary Export Market'
    END,

    CASE
        WHEN TEMPERATURE > 8 THEN 1500
        WHEN TEMPERATURE > 5 THEN 3200
        ELSE 4700
    END,

    CASE
        WHEN TEMPERATURE > 8 THEN 'Immediate Reroute'
        WHEN TEMPERATURE > 5 THEN 'Monitor Every Hour'
        ELSE 'Continue Standard Route'
    END,

    TIMESTAMP

FROM RAW.CONTAINER_SENSOR_DATA r

WHERE NOT EXISTS (
    SELECT 1
    FROM ANALYTICS.CONTAINER_ANALYTICS a
    WHERE a.CONTAINER_ID = r.CONTAINER_ID
      AND a.TIMESTAMP = r.TIMESTAMP
);

-- Start the automated task

ALTER TASK UPDATE_ANALYTICS RESUME;