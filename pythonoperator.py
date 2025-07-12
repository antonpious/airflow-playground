from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta
import logging


def hello_world():
    msg = "Hello world Python"
    logging.info(msg)

# the name of the dag can't have spaces
with DAG(
    "Python_Operator_Example",
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        "depends_on_past": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
        
    },
    description="A simple python operator DAG",
    schedule=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["pythonoperator"],
) as dag:

    t1 = PythonOperator(
            task_id = 'python_task',
            python_callable = hello_world
        )