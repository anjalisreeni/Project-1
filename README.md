
# Project 1 - AtmoSync: Micro-Climate Arbitrage Analytics

## Problem Statement

Traditional supply chain analytics rely on standard transit times and macro-weather forecasts. They fail to monitor real-time, hyper-local micro-climate changes (such as sudden temperature or humidity variations inside refrigerated shipping containers), leading to spoilage of agricultural commodities before they reach the market.

## Use Case

A commodities trader uses the **AtmoSync Dashboard** to monitor refrigerated shipments in real time.

The streaming pipeline continuously analyzes IoT sensor data from each container. If a container's environmental conditions deviate from the safe range, the system detects the increased spoilage risk and alerts the trader. This enables shipment rerouting to a nearby secondary market, reducing losses and maximizing profit.

## Project Architecture

```
IoT Simulator
      │
      ▼
Real-Time Data Generator
      │
      ▼
Apache Kafka
      │
      ▼
Snowflake
      │
      ▼
dbt
      │
      ▼
Apache Superset Dashboard
```

---

## Key Modules

### Streaming Ingestion (Apache Kafka)
- Generate simulated IoT sensor data
- Stream container telemetry in real time

### Cloud Data Warehouse (Snowflake)
- Store raw IoT streams
- Store historical shipment data

### Data Transformation (dbt)
- Clean raw streaming data
- Build analytical models
- Calculate spoilage metrics and business insights

### Visualization (Apache Superset)
- Live container monitoring
- Shipment health dashboard
- Risk alerts
- Operational analytics

---

## Current Progress

### Completed

- Historical IoT dataset generator (`iot_simulator.py`)
- Real-time IoT data generator (`realtime_generator.py`)
- Generated dataset with 10,000 sensor records
- Risk Score calculation
- Alert Status generation
- Live timestamp updates
- Sensor value simulation

### In Progress

- Kafka Producer
- Kafka Consumer
- Snowflake Integration
- dbt Models
- Apache Superset Dashboard

---

## Dataset Features

- Container ID
- Shipment ID
- Fruit Type
- Origin
- Destination
- Temperature
- Humidity
- Vibration
- Battery Level
- Door Status
- Container Status
- Latitude
- Longitude
- Timestamp
- Risk Score *(Generated in Real-Time)*
- Alert Status *(Generated in Real-Time)*

---

## Technologies Used

- Python
- Pandas
- Apache Kafka
- Snowflake
- dbt
- Apache Superset
- Git & GitHub

---

## Repository Structure

```
Project-1/
│
├── Data/
├── Simulator/
│   ├── iot_simulator.py
│   └── realtime_generator.py
├── Producer/
├── Consumer/
├── Snowflake/
├── dbt/
├── Dashboard/
├── Notebook/
└── README.md
```

---

## Objective

Develop a scalable, real-time cold-chain monitoring system capable of streaming IoT sensor data, analyzing spoilage risks, and supporting data-driven logistics decisions through an end-to-end ELT pipeline.