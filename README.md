
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
  - Stream
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

## 📄 Page 3 – Live Risk & Business Analytics

 KPI Cards

- Average Risk Score
- Estimated Financial Loss
- Arbitrage Profit

 Interactive Slicers

- Fruit Type
- Origin
- Destination
- Spoilage Risk

Visualizations

- Live Temperature Trend
- Spoilage Risk Distribution
- Recommended Market Distribution

### Live Monitoring Table

Displays real-time shipment information including:

- Container ID
- Fruit Type
- Temperature
- Humidity
- Risk Score
- Spoilage Risk
- Recommended Action

The dashboard updates with newly streamed sensor records after refreshing the report.

---

# 📊 7. Snowflake Data Pipeline & Analytics

Developed a Snowflake-based data pipeline to transform raw IoT sensor data into business-ready analytics for refrigerated supply chain monitoring.

## 📄 create_raw_table.sql

Created the RAW data layer for ingesting live sensor data.

### Features

- Created `RAW` schema
- Created `CONTAINER_SENSOR_DATA` table
- Designed schema for:
  - Shipment Information
  - Environmental Sensor Data
  - Device Health
  - GPS Coordinates
  - Timestamp
  - Route Information
- Used as the landing table for streamed IoT sensor records

---

## 📄 analytics_transformation.sql

Developed the analytics layer to generate operational insights from raw sensor data.

### Features

- Created `ANALYTICS` schema
- Created `CONTAINER_ANALYTICS` table
- Loaded transformed data from the RAW layer
- Calculated Risk Score using:
  - Temperature
  - Humidity
  - Vibration
  - Battery Level
- Classified containers into:
  - Safe
  - Warning
  - Critical
- Estimated:
  - Time to Spoilage
  - Estimated Financial Loss
  - Arbitrage Profit
- Recommended:
  - Best Destination Market
  - Operational Action
- Implemented an automated Snowflake Task (`UPDATE_ANALYTICS`) to continuously move newly streamed records from the RAW layer into the Analytics layer every minute
- Added monitoring queries for task history, execution status and row count validation

---

# 🌐 8. Real-Time Snowflake Streaming

Designed a real-time streaming pipeline using Python and Snowflake.

### Features

- Connected Python application with Snowflake
- Streamed IoT sensor records into `RAW.CONTAINER_SENSOR_DATA`
- Simulated continuous live sensor data using timed inserts
- Automatically updated the Analytics layer using a scheduled Snowflake Task
- Enabled near real-time analytics for Power BI dashboard refresh

# 📁 Project Structure

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
│   ├── page_2_dashboard.jpg
│   └── page_3_dashboard.jpg
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
├── Stream/
│   └── stream_to_snowflake.py
│
├── SQL/
│   ├── create_raw_table.sql
│   ├── analytics_transformation.sql
│   └── queries_dashboard.sql
│
├── .gitignore
├── README.md
└── requirements.txt
```

---



# 🙌 Acknowledgement

This project was developed as part of the **Infotact AtmoSync** team project.

The work presented in this branch represents **my individual contributions**, including:

- Repository Structure
- Python IoT Sensor Simulator
- Exploratory Data Analysis (EDA)
- Feature Engineering
- SQL Business Analytics
- Snowflake Data Pipeline
- Real-Time Data Streaming
- Three-Page Power BI Dashboard
- Analytics Transformation 

## 👤 Author

**Sayam Stuti Shuvadarsini**
## Connect with me

- 💼 LinkedIn: www.linkedin.com/in/sayam-stuti-shuvadarsini
- 💻 GitHub: https://github.com/sayamstuti 
- 📧 Email: sayamstuti594@gmail.com 