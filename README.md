
# 🌍 AtmoSync – Micro-Climate Arbitrage Analytics

> A real-time IoT-driven analytics platform that monitors shipping container conditions, predicts spoilage risk, and enables data-driven rerouting decisions using streaming data engineering and cloud analytics.

---

## 📌 Problem Statement

Traditional supply chain analytics rely on fixed transit schedules and macro-level weather forecasts. They fail to capture **real-time, hyper-local micro-climate changes** occurring inside shipping containers. Sudden fluctuations in temperature, humidity, or air quality can rapidly degrade perishable commodities before they reach the market, leading to significant financial losses.

**AtmoSync** solves this challenge by continuously monitoring IoT sensor data, detecting abnormal environmental conditions, calculating spoilage risk, and providing real-time insights to support timely business decisions.

---

## 💡 Use Case

A commodities trader at **Infotact** monitors the AtmoSync dashboard while tracking multiple shipments.

The streaming pipeline detects that **Container A** is experiencing an unexpected rise in internal temperature, accelerating the spoilage of the avocados inside.

AtmoSync immediately analyzes the incoming sensor data, estimates the spoilage rate, and identifies a profitable **Spoilage Arbitrage** opportunity. Instead of allowing the shipment to continue to its original destination, the system recommends rerouting it to a nearby secondary market where the produce can still be sold at a premium price before its quality deteriorates.

This enables organizations to reduce wastage, improve operational efficiency, and maximize financial returns through real-time analytics.

---

# 🚀 Project Architecture

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

# 🛠️ Tech Stack

- Python
- Apache Kafka
- Snowflake
- SQL
- dbt
- Apache Superset
- Power BI
- Git & GitHub

---

# 📂 Project Structure

```
Project-1
│
├── Dashboard
│   └── dashboard.pbix
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
│
├── Kafka
│   ├── producer.py
│   ├── consumer.py
│   └── risk_utils.py
│
├── Simulator
│   ├── iot_simulator.py
│   └── snowflake_connection.py
│
├── SQL
│   └── setup_snowflake.sql
│
├── Notebooks
│   ├── EDA_IoT_Simulator.ipynb
│   └── Feature_Engineering.ipynb
│
├── config.py
├── requirements.txt
└── README.md
```

---

# ✨ Key Features

- Real-time IoT sensor simulation
- Kafka-based streaming data pipeline
- Cloud data storage using Snowflake
- SQL-based warehouse initialization
- Feature engineering and exploratory data analysis
- Risk assessment using sensor analytics
- Interactive dashboard for operational monitoring
- Scalable and modular data engineering workflow

---

# 👥 Team Members & Contributions

## 👩 Sayam Stuti Shuvadarsini

**Data Analytics & IoT Simulation**

- Developed the IoT Sensor Simulator
- Generated mock environmental sensor data
- Performed Exploratory Data Analysis (EDA)
- Implemented Feature Engineering
- Designed and developed the Power BI Dashboard
- Created project documentation
- Organized the repository structure and project integration

---

## 👩 Jiya Pendhari

**Snowflake Integration**

- Configured Snowflake database connection
- Developed Snowflake data insertion module
- Created Snowflake warehouse, schema, and table setup
- Implemented centralized configuration for Snowflake connectivity

**Files**
- `Simulator/snowflake_connection.py`
- `SQL/setup_snowflake.sql`
- `config.py`

---

## 👨 Neel

**Kafka Streaming Pipeline**

- Developed Kafka Producer
- Developed Kafka Consumer
- Implemented Risk Utility Module

**Files**
- `Kafka/producer.py`
- `Kafka/consumer.py`
- `Kafka/risk_utils.py`

---

## 👩 Anjali Sreeni

**Project Lead & Repository Management**

- Repository management
- Team coordination
- Overall project integration

---

# 📊 Dashboard Overview

The dashboard provides real-time insights into:

- Temperature Monitoring
- Humidity Analysis
- Pressure Monitoring
- CO₂ Gas Levels
- PM2.5 Monitoring
- PM10 Monitoring
- Container Health Status
- Sensor Performance
- Operational KPIs

---

# 🔄 Workflow

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
SQL / dbt Transformations
      │
      ▼
Apache Superset / Power BI Dashboard
```

---

# 🎯 Expected Outcomes

- Build a scalable real-time streaming analytics pipeline.
- Monitor container conditions using IoT telemetry.
- Store and manage streaming data in Snowflake.
- Perform data transformation and feature engineering.
- Generate actionable insights through interactive dashboards.
- Support business decisions using Spoilage Arbitrage analytics.

---

# 🚀 Future Enhancements

- Complete dbt transformation models
- Deploy Apache Superset for live dashboards
- Automated pipeline orchestration
- Slack and Email alert system
- Machine Learning based spoilage prediction
- Route optimization recommendations
- Cloud deployment using Docker and Kubernetes

---

# 📄 License

This project was developed as part of the **Infotact Data Engineering & Analytics Internship Program**.

---

⭐ **If you found this project interesting, consider giving this repository a Star!**