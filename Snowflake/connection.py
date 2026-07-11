"""
Snowflake Connection Helper
Establishes a connection to Snowflake using environment variables for credentials.
"""
import os
import snowflake.connector


def get_connection():
    return snowflake.connector.connect(
        user=os.environ.get("SNOWFLAKE_USER"),
        password=os.environ.get("SNOWFLAKE_PASSWORD"),
        account=os.environ.get("SNOWFLAKE_ACCOUNT"),
        warehouse=os.environ.get("SNOWFLAKE_WAREHOUSE", "COMPUTE_WH"),
        database=os.environ.get("SNOWFLAKE_DATABASE", "IOT_DB"),
        schema=os.environ.get("SNOWFLAKE_SCHEMA", "PUBLIC"),
    )


def run_query(query: str):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(query)
        return cur.fetchall()
    finally:
        conn.close()


if __name__ == "__main__":
    result = run_query("SELECT CURRENT_VERSION()")
    print(result)
