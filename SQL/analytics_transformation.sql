-- =====================================================
-- Week 3 : Analytics Layer
-- Project : AtmoSync
-- =====================================================

USE DATABASE ATMOSYNC_DB;

CREATE SCHEMA IF NOT EXISTS ANALYTICS;

USE SCHEMA ANALYTICS;

CREATE TABLE IF NOT EXISTS CONTAINER_ANALYTICS (

    ID INTEGER,

    TIMESTAMP TIMESTAMP,

    TEMPERATURE FLOAT,

    HUMIDITY FLOAT,

    PRESSURE FLOAT,

    CO2_GAS INTEGER,

    PM2_5 FLOAT,

    PM10 FLOAT,

    DAYTIME STRING,

    SPOILAGE_SCORE NUMBER(5,2),

    SPOILAGE_RISK STRING,

    TIME_TO_SPOILAGE NUMBER(5,2),

    ESTIMATED_LOSS NUMBER(10,2),

    ARBITRAGE_PROFIT NUMBER(10,2),

    RECOMMENDED_MARKET STRING,

    RECOMMENDED_ACTION STRING

);
-- Create Market Pricing Table
CREATE TABLE IF NOT EXISTS MARKET_PRICING (

    MARKET_NAME STRING,

    MARKET_VALUE NUMBER(10,2)

);

-- Insert Market Prices
INSERT INTO MARKET_PRICING
VALUES
('Primary Export Market',5000),
('Regional Distribution Center',4500),
('Nearest Local Market',3800);

-- Check the data
SELECT * FROM MARKET_PRICING;


TRUNCATE TABLE CONTAINER_ANALYTICS;

INSERT INTO CONTAINER_ANALYTICS

WITH SENSOR_ANALYTICS AS (

    SELECT
        ID,
        TIMESTAMP,
        TEMPERATURE,
        HUMIDITY,
        PRESSURE,
        CO2_GAS,
        PM2_5,
        PM10,
        DAYTIME,

        (
    CASE
        WHEN TEMPERATURE <= 5 THEN 5
        WHEN TEMPERATURE <= 8 THEN 15
        WHEN TEMPERATURE <= 12 THEN 30
        ELSE 40
    END +

    CASE
        WHEN HUMIDITY <= 60 THEN 5
        WHEN HUMIDITY <= 75 THEN 15
        ELSE 30
    END +

    CASE
        WHEN CO2_GAS <= 400 THEN 5
        WHEN CO2_GAS <= 600 THEN 10
        ELSE 15
    END +

    CASE
        WHEN PM2_5 <= 20 THEN 5
        ELSE 10
    END +

    CASE
        WHEN PM10 <= 30 THEN 5
        ELSE 10
    END

) AS SPOILAGE_SCORE

    FROM RAW.CONTAINER_SENSOR_DATA

),
--------------------------------------------------
--  Determine Market Name first
--------------------------------------------------
FINAL_ANALYTICS AS (

SELECT

    *,

    CASE
        WHEN SPOILAGE_SCORE >= 70 THEN 'Nearest Local Market'
        WHEN SPOILAGE_SCORE >= 40 THEN 'Regional Distribution Center'
        ELSE 'Primary Export Market'
    END AS MARKET_NAME

FROM SENSOR_ANALYTICS

)

SELECT

    f.ID,
    f.TIMESTAMP,
    f.TEMPERATURE,
    f.HUMIDITY,
    f.PRESSURE,
    f.CO2_GAS,
    f.PM2_5,
    f.PM10,
    f.DAYTIME,

    f.SPOILAGE_SCORE,

    --------------------------------------------------
    -- Spoilage Risk
    --------------------------------------------------
    CASE
        WHEN f.SPOILAGE_SCORE >= 70 THEN 'Critical'
        WHEN f.SPOILAGE_SCORE >= 40 THEN 'Warning'
        ELSE 'Safe'
    END,

    --------------------------------------------------
    --  Hours remaining
    --------------------------------------------------
    CASE
        WHEN f.SPOILAGE_SCORE <= 30 THEN 72
        WHEN f.SPOILAGE_SCORE <= 50 THEN 48
        WHEN f.SPOILAGE_SCORE <= 70 THEN 24
        ELSE 8
    END,

    --------------------------------------------------
    --  Estimated Loss
    --------------------------------------------------
    CASE
        WHEN f.SPOILAGE_SCORE <= 30 THEN 250
        WHEN f.SPOILAGE_SCORE <= 50 THEN 750
        WHEN f.SPOILAGE_SCORE <= 70 THEN 1500
        ELSE 2500
    END,

    --------------------------------------------------
    --  Arbitrage Profit from MARKET_PRICING table
    --------------------------------------------------
    (
        m.MARKET_VALUE -

        CASE
            WHEN f.SPOILAGE_SCORE <= 30 THEN 250
            WHEN f.SPOILAGE_SCORE <= 50 THEN 750
            WHEN f.SPOILAGE_SCORE <= 70 THEN 1500
            ELSE 2500
        END

    ) AS ARBITRAGE_PROFIT,

    --------------------------------------------------
    --  Uses lookup table instead of hardcoding
    --------------------------------------------------
    f.MARKET_NAME,

    --------------------------------------------------
    --  Better Action Messages
    --------------------------------------------------
    CASE
        WHEN f.SPOILAGE_SCORE >= 70 THEN 'Immediate Reroute & Priority Delivery'
        WHEN f.SPOILAGE_SCORE >= 40 THEN 'Monitor Every Hour'
        ELSE 'Continue Standard Route'
    END

FROM FINAL_ANALYTICS f

--------------------------------------------------
--  Join with Market Pricing table
--------------------------------------------------
JOIN MARKET_PRICING m
ON f.MARKET_NAME = m.MARKET_NAME;

SELECT * FROM CONTAINER_ANALYTICS;

