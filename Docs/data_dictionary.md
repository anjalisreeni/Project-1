
# Data Dictionary

This document describes the fields used in the AtmoSync IoT sensor dataset.

| Column | Description |
|---------|-------------|
| container_id | Unique container identifier |
| shipment_id | Unique shipment identifier |
| fruit_type | Type of fruit being transported |
| origin | Shipment origin city |
| destination | Shipment destination city |
| temperature | Container temperature (°C) |
| humidity | Humidity inside the container (%) |
| vibration | Vibration level during transit |
| battery_level | IoT device battery percentage |
| door_status | Door status (Open/Closed) |
| container_status | Shipment status |
| latitude | GPS latitude |
| longitude | GPS longitude |
| timestamp | Date and time of sensor reading |
| risk_level | Engineered spoilage risk category |
| battery_status | Engineered battery health category |
| temperature_status | Temperature condition category |
| route | Shipment route (Origin → Destination) |
| hour | Hour extracted from timestamp |
| day | Day extracted from timestamp |
| month | Month extracted from timestamp |
| weekday | Weekday extracted from timestamp |