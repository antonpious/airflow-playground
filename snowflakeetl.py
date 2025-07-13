from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta
import logging
from dotenv import load_dotenv
import os

# This folder structure is present under the DAG folder
# So we are making use of this structure
# The current things to do is to using the my_company structure 
# This way one can test the python file for error before
# copying to the DAG folder
# The python path already has the DAG folder path in it
from etl.snowflake_etl_example.calculator import add

load_dotenv()


def snowflake_etl():
    snowflake_account = os.getenv("SNOWFLAKE_USERNAME")
    result = add(4,6)
    msg = f"The environment variable account:{snowflake_account} and result: {result}"
    logging.info(msg)

# the name of the dag can't have spaces
with DAG(
    "snowflake_etl_example",
    
    default_args={
        "depends_on_past": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
        
    },
    description="A snowflake ETL pipeline",
    schedule=timedelta(days=1),
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["snowflake","etl"],
) as dag:

    t1 = PythonOperator(
            task_id = 'insert_snowflake',
            python_callable = snowflake_etl
        )