# Dashboard

Visualization layer for the IoT sensor pipeline. Connect this to Snowflake (or the dbt-modeled tables) using your BI tool of choice (e.g. Streamlit, Tableau, Power BI, Looker).

## Suggested next steps
- Build a Streamlit app that queries `dbt`-modeled tables in Snowflake
- Add charts for temperature, humidity, and pressure trends per sensor
- Add alerting for out-of-range sensor readings
