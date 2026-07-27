
# Feature Engineering

To improve analytical capabilities, additional business-oriented features were created from the raw IoT sensor data.

## Engineered Features

- **Risk Level** – Categorizes containers into Low, Medium, or High risk based on environmental conditions.
- **Battery Status** – Classifies IoT device battery health.
- **Temperature Status** – Indicates whether the recorded temperature is within the safe operating range.
- **Route** – Combines shipment origin and destination into a single route field.
- **Timestamp Features** – Extracted Hour, Day, Month, and Weekday from the timestamp for time-based analysis.

The transformed dataset was saved as:

```
sensor_data_feature_engineered.csv
```

These engineered features support SQL analytics and dashboard visualizations.