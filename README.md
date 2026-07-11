# PROJECT-1

An end-to-end IoT sensor data pipeline: simulate sensor readings, stream them through Kafka, load them into Snowflake, transform them with dbt, and visualize them on a dashboard.

## Architecture

```
Simulator (iot_simulator.py)
        │
        ▼
   Kafka Producer  ──►  Kafka Topic  ──►  Kafka Consumer
                                                │
                                                ▼
                                            Snowflake
                                                │
                                                ▼
                                              dbt
                                                │
                                                ▼
                                           Dashboard
```

## Project structure

- **Dashboard/** — visualization layer
- **Data/** — sample/raw sensor data (`sensor_data.csv`)
- **dbt/** — dbt project for transforming raw Snowflake data
  - **models/** — dbt models
- **Docs/** — documentation and diagrams
- **Kafka/** — producer and consumer scripts
- **Notebooks/** — exploratory analysis notebooks
- **Simulator/** — synthetic IoT sensor data generator
- **Snowflake/** — connection helper and table DDL

## Getting started

1. Create and activate a virtual environment
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the simulator to generate sensor data:
   ```bash
   python Simulator/iot_simulator.py
   ```
4. Start Kafka locally (or point to your broker) and run the producer/consumer:
   ```bash
   python Kafka/producer.py
   python Kafka/consumer.py
   ```
5. Set Snowflake credentials as environment variables and create tables:
   ```bash
   python Snowflake/connection.py
   ```
   ```sql
   -- run Snowflake/create_tables.sql in your Snowflake worksheet
   ```
6. Run dbt models:
   ```bash
   cd dbt
   dbt run
   ```

## Environment variables

| Variable | Description |
|---|---|
| `SNOWFLAKE_USER` | Snowflake username |
| `SNOWFLAKE_PASSWORD` | Snowflake password |
| `SNOWFLAKE_ACCOUNT` | Snowflake account identifier |
| `SNOWFLAKE_WAREHOUSE` | Snowflake warehouse (default: `COMPUTE_WH`) |
| `SNOWFLAKE_DATABASE` | Snowflake database (default: `IOT_DB`) |
| `SNOWFLAKE_SCHEMA` | Snowflake schema (default: `PUBLIC`) |

## License

Add your license here.
