
# Project Overview

# AtmoSync – Micro-Climate Arbitrage Analytics

AtmoSync is a real-time supply chain analytics project designed to monitor refrigerated agricultural shipments using IoT sensor data. The platform continuously tracks container conditions, predicts spoilage risk, estimates financial impact, and provides actionable insights to support better logistics decisions.

## Problem Statement

Traditional cold-chain logistics systems cannot continuously monitor the environmental conditions inside refrigerated containers. Variations in temperature, humidity, vibration, and equipment health may lead to product spoilage and financial losses before shipments reach their destinations.

## Solution

AtmoSync addresses this challenge by building an end-to-end analytics pipeline that:

- Simulates IoT sensor data for refrigerated containers.
- Streams live sensor data into Snowflake.
- Stores raw telemetry in a cloud data warehouse.
- Transforms raw data into business-ready analytics using SQL.
- Calculates risk score, spoilage risk, estimated loss, and arbitrage profit.
- Automates analytics updates using Snowflake Tasks.
- Presents interactive Power BI dashboards for operational monitoring and business insights.

## Key Features

- Real-time IoT sensor simulation
- Live data streaming to Snowflake
- Snowflake analytics transformation pipeline
- Automated analytics updates using Snowflake Tasks
- Risk score and spoilage prediction
- Estimated loss and arbitrage profit analysis
- Interactive three-page Power BI dashboard

## Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Power BI, Matplotlib |
| Database & Cloud | Snowflake |
| SQL | Snowflake SQL |
| Streaming | Python Real-Time Data Streaming |
| Version Control | Git & GitHub |
