
#  AtmoSync – Micro-Climate Arbitrage Analytics

> A real-time IoT-driven analytics platform that monitors shipping container conditions, predicts spoilage risk, and enables data-driven rerouting decisions using streaming data engineering and cloud analytics.

---
##  Table of Contents

- [ Problem Statement](#-problem-statement)
- [ Use Case](#-use-case)
- [ Project Architecture](#-project-architecture)
- [ Tech Stack](#️-tech-stack)
- [ Project Structure](#-project-structure)
- [ Key Features](#-key-features)
- [ Team Members & Contributions](#-team-members--contributions)
- [ Dashboard Overview](#-dashboard-overview)
- [ Workflow](#-workflow)
- [ Expected Outcomes](#-expected-outcomes)
- [ Future Enhancements](#-future-enhancements)
- [ License](#-license)

##  Problem Statement

Traditional supply chain analytics rely on fixed transit schedules and macro-level weather forecasts. They fail to capture **real-time, hyper-local micro-climate changes** occurring inside shipping containers. Sudden fluctuations in temperature, humidity, or air quality can rapidly degrade perishable commodities before they reach the market, leading to significant financial losses.

**AtmoSync** solves this challenge by continuously monitoring IoT sensor data, detecting abnormal environmental conditions, calculating spoilage risk, and providing real-time insights to support timely business decisions.

---

##  Use Case

A commodities trader at **Infotact** monitors the AtmoSync dashboard while tracking multiple shipments.

The streaming pipeline detects that **Container A** is experiencing an unexpected rise in internal temperature, accelerating the spoilage of the avocados inside.

AtmoSync immediately analyzes the incoming sensor data, estimates the spoilage rate, and identifies a profitable **Spoilage Arbitrage** opportunity. Instead of allowing the shipment to continue to its original destination, the system recommends rerouting it to a nearby secondary market where the produce can still be sold at a premium price before its quality deteriorates.

This enables organizations to reduce wastage, improve operational efficiency, and maximize financial returns through real-time analytics.

---

#  Project Architecture

```
IoT Sensor Simulator
        │
        ▼
 Apache Kafka
 (Producer → Consumer)
        │
        ▼
 Snowflake Data Warehouse
        │
        ▼
 SQL / dbt Transformations
        │
        ▼
 Analytics & KPIs
        │
        ▼
 Apache Superset / Power BI Dashboard
```

---

#  Tech Stack

- Python
- Pandas & NumPy
- Matplotlib
- Snowflake
- SQL
- Power BI
- Apache Kafka
- Git & GitHub

---

#  Project Structure

```text
Project-1
│
├── Dashboard
│   └── Atmosync_dashboard.pbix
│
├── Data
│   ├── sensor_data.csv
│   └── sensor_data_feature_engineered.csv
│
├── Docs
│   ├── dashboard_guide.md
│   ├── data_dictionary.md
│   ├── feature_engineering.md
│   └── project_overview.md
│
├── Images
│   ├── page_1_dashboard.jpg
│   ├── page_2_dashboard.jpg
│   └── page_3_dashboard.jpg
│
├── Kafka
│   ├── producer.py
│   ├── consumer.py
│   └── risk_utils.py
│
├── Notebooks
│   ├── EDA_IoT_Simulator.ipynb
│   └── Feature_Engineering.ipynb
│
├── Simulator
│   ├── iot_simulator.py
│   └── snowflake_connection.py
│
├── SQL
│   ├── analytics_transformation.sql
│   ├── create_raw_table.sql
│   ├── queries_dashboard.sql
│   └── setup_snowflake.sql
│
├── Stream
│   └── stream_to_snowflake.py
│
├── config.py
├── requirements.txt
└── README.md

```

---

#  Key Features

- Real-time IoT sensor simulation
- Live data streaming to Snowflake
- Automated analytics transformation using Snowflake Tasks
- Spoilage risk assessment and business KPI generation
- SQL-based data analytics and reporting
- Interactive three-page Power BI dashboard
- Estimated loss and arbitrage profit analysis
- Modular data engineering pipeline

---

#  Team Members & Contributions

##  Sayam Stuti Shuvadarsini

**Data Analytics, Snowflake Pipeline, IoT Simulation & Dashboard Development**

- Developed the IoT Sensor Simulator
- Generated mock environmental sensor data
- Performed Exploratory Data Analysis (EDA)
- Implemented Feature Engineering
- Built SQL analytics queries
- Developed Snowflake analytics transformation pipeline
- Implemented real-time data streaming into Snowflake
- Designed and developed a three-page interactive Power BI Dashboard
- Created project documentation
- Organized the repository structure and project integration

**Files**

- `Simulator/iot_simulator.py`
- `Stream/stream_to_snowflake.py`
- `SQL/create_raw_table.sql`
- `SQL/analytics_transformation.sql`
- `SQL/queries_dashboard.sql`
- `Dashboard/Atmosync_dashboard.pbix`
- `Notebooks/EDA_IoT_Simulator.ipynb`
- `Notebooks/Feature_Engineering.ipynb`
- `Data/sensor_data.csv`
- `Data/sensor_data_feature_engineered.csv`
- `Docs/dashboard_guide.md`
- `Docs/data_dictionary.md`
- `Docs/feature_engineering.md`
- `Docs/project_overview.md`
- `Images/page_1_dashboard.jpg`
- `Images/page_2_dashboard.jpg`
- `Images/page_3_dashboard.jpg`

---

##  Jiya Pendhari

**Snowflake Integration & Live Data Pipeline**

### Responsibilities

- Configured the Snowflake account and established secure Python connectivity.
- Created the Snowflake warehouse, database, schema, and container sensor data table.
- Developed Python modules for Snowflake connection and live data insertion.
- Implemented automated sensor data generation and continuous insertion into Snowflake.
- Centralized database connection settings using `config.py`.
- Validated successful storage of real-time IoT sensor data in Snowflake.

**Files**
- `Simulator/snowflake_connection.py`
- `SQL/setup_snowflake.sql`
- `config.py`

---

##  Neel

**Kafka Streaming Pipeline**

- Developed Kafka Producer
- Developed Kafka Consumer
- Implemented Risk Utility Module

**Files**
- `Kafka/producer.py`
- `Kafka/consumer.py`
- `Kafka/risk_utils.py`

---

##  Anjali Sreeni

**Project Lead & Repository Management**

- Repository management
- Team coordination
- Overall project integration

---


#  Dashboard Overview

The project includes a **three-page interactive Power BI dashboard** for monitoring refrigerated container health and supporting logistics decisions.

### Features

- KPI Cards
- Live Temperature Trend
- Shipment & Fruit Analytics
- Spoilage Risk Distribution
- Estimated Loss & Arbitrage Profit
- Destination-wise Profit Analysis
- Live Container Alerts
- Interactive Filters

---

#  Workflow

```
IoT Simulator
      │
      ▼
Kafka Producer
      │
      ▼
Kafka Topic
      │
      ▼
Kafka Consumer
      │
      ▼
Snowflake
      │
      ▼
SQL Transformations
      │
      ▼
 Power BI Dashboard
```

---

#  Expected Outcomes

- Real-time monitoring of refrigerated container conditions.
- Early detection of spoilage risks using IoT sensor data.
- Support data-driven logistics and rerouting decisions.
- Deliver interactive analytics through Power BI dashboards.
- Demonstrate an end-to-end data engineering and analytics pipeline.
---


---

#  License

This project was developed as part of the **Infotact Data Engineering & Analytics Internship Program**.

---

⭐ **If you found this project interesting, consider giving this repository a Star!**
