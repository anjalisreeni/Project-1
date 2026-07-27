
# 🌦️ AtmoSync – Micro-Climate Arbitrage Analytics

> A real-time supply chain analytics platform that monitors refrigerated agricultural shipments using IoT sensor data, enabling early spoilage detection and smarter logistics decisions.

---

# 👨‍💻 My Contributions

This branch contains my individual contributions to the AtmoSync project.

## ✅ 1. Repository Structure

- Created the initial repository structure
- Organized folders for:
  - Data
  - Notebooks
  - Docs
  - Images
  - Simulator
  - Snowflake
  - Dashboard
  - Documentation
  - Notebook
  - README
  - requirement.txt

---

# 📡 2. Python IoT Sensor Simulator

Designed and developed a Python-based IoT simulator that generates realistic refrigerated container sensor data.

### Dataset Statistics

- **10,000 Sensor Records**
- **100 Containers**
- **1000 Shipments**
- **10 Fruit Types**
- **8 Indian Cities**

### Generated Features

### Shipment Information

- Container ID
- Shipment ID
- Fruit Type
- Origin
- Destination

### Environmental Sensors

- Temperature
- Humidity
- Vibration

### Device Health

- Battery Level
- Door Status

### Logistics

- Container Status
- GPS Coordinates
- Historical Timestamp

The simulator mimics real refrigerated container telemetry for analytics and dashboard development.

---

# 📊 3. Exploratory Data Analysis (EDA)

Performed comprehensive exploratory analysis on the generated IoT dataset.

### Analysis Performed

- Humidity Distribution
- Fruit Distribution
- Door Status Analysis
- Shipment Origin Distribution
- Correlation Heatmap
- Average Temperature by Fruit Type

These analyses helped identify shipment patterns and validate generated sensor data.

---

# ⚙️ 4. Feature Engineering

Created additional business-oriented features to improve analytics.

### Engineered Features

- Risk Level
- Battery Status
- Temperature Status
- Shipment Route
- Timestamp Features
  - Hour
  - Day
  - Month
  - Weekday

The transformed dataset was exported as:

```
sensor_data_feature_engineered.csv
```

---

# 🗄️ 5. SQL Analytics

Designed SQL queries to extract operational insights.

### Queries Implemented

- Total Shipments
- Total Containers
- Average Temperature
- Average Humidity
- Average Battery
- Shipment Status Distribution
- Fruit-wise Shipments
- Average Temperature by Fruit
- Highest Temperature Containers
- High Risk Containers
- Battery Status Distribution
- Average Temperature by Route
- Origin-wise Shipments
- Destination-wise Shipments
- Hourly Sensor Readings
- Low Battery Containers
- Temperature Status Distribution

---

# 📈 6. Power BI Dashboard

Designed an interactive two-page dashboard to monitor container health and shipment performance.

---

## 📄 Page 1 – Operational Monitoring

Features

- KPI Cards
  - Total Containers
  - Total Shipments
  - Average Temperature
  - Average Humidity
  - Average Battery
  - Sensor Readings

- Temperature Trend

- Container Distribution by Fruit

- Container Status Distribution

- Top Fruits by Average Temperature

- Operational Insights Panel


---

## 📄 Page 2 – Historical & Logistics Analysis

Features

- Shipment Distribution by Origin (Map)

- Shipment Distribution by Destination

- Container Status by Origin

- Environmental Summary

- Operational Insights


---

# 📁 Project Structure

```
## 📂 Project Structure

```text
## 📂 Project Structure

```text
AtmoSync/
│
├── Dashboard/
│   └── dashboard.pbix
│
├── Data/
│   ├── sensor_data.csv
│   └── sensor_data_feature_engineered.csv
│
├── Docs/
│   ├── project_overview.md
│   ├── data_dictionary.md
│   ├── feature_engineering.md
│   └── dashboard_guide.md
│
├── Images/
│   ├── page_1_dashboard.jpg
│   └── page_2_dashboard.jpg
│
├── Notebooks/
│   ├── EDA_IoT_simulator.ipynb
│   └── Feature_Engineering.ipynb
│
├── Presentation/
│   └── AtmoSync_Project_Presentation.pdf
│
├── Simulator/
│   ├── __init__.py
│   ├── iot_simulator.py
│   └── realtime_simulator.py
│
├── SQL/
│   └── queries_dashboard.sql
│
├── .gitignore
├── README.md
└── requirements.txt

```
```

---

# 📊 Key Features

- Realistic IoT Sensor Data Generation
- Refrigerated Container Monitoring
- Environmental Analytics
- Shipment Route Analysis
- Risk Detection
- SQL Business Analytics
- Interactive Power BI Dashboard
- Supply Chain Insights

---

# 🎯 Future Scope

- Live Kafka Streaming
- Snowflake Integration
- dbt Transformation Models
- Apache Superset Live Dashboard
- Predictive Spoilage Detection
- Machine Learning Risk Prediction
- Real-time Alert System

---

# 🙌 Acknowledgement

This project was developed as part of the **Infotact AtmoSync** team project.

The work presented in this branch represents **my individual contributions**, including:

- Repository Structure
- Python IoT Sensor Simulator
- Exploratory Data Analysis
- Feature Engineering
- SQL Analytics
- Two-page Power BI Dashboard