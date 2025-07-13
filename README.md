# airflow-playground
Showcase Airflow features


# install airflow in standalone mode in a folder in your local computer
follow the instructions present [here](https://airflow.apache.org/docs/apache-airflow/stable/start.html)


# Copy the requirements.txt to the airflow root directory
`cp requirements.txt /Users/anton/Software/airflow`

## copy the file to the dag folder

`cp tutorial.py /Users/anton/Software/airflow/dags`  
`cp pythonoperator.py /Users/anton/Software/airflow/dags`  

organizing airflow DAG folder  
create two folders
ETL  
ELT  

When we do the ML we can create another folder called 
ML  

For each of the dag create a folder instead of a file.  
This way we can put the .env and other module within this dag.

`cp snowflakeetl.py /Users/anton/Software/airflow/dags/etl/snowflake_etl_example` 
`cp .env /Users/anton/Software/airflow/dags/etl/snowflake_etl_example`
`cp calculator.py /Users/anton/Software/airflow/dags/etl/snowflake_etl_example`    


have to check how to load a local package with the DAG

go to the standalone installation folder for airflow  

activate the virtual environment  
`source .venv/bin/activate`  

run airflow  
`airflow standalone`  

This should load the dags in the dags folder  

The credential for logging to the airflow web server UI is present in the file  
`cat simple_auth_manager_passwords.json.generated`  

The server URL is 
`http://localhost:8080`  


## copy the requirements to the airflow server location   
`cp requirements.txt /Users/anton/Software/airflow`

## install the requirements in airflow virtual environment  
`uv pip install -r requirements.txt`

Note:  
You have to unpause the DAG in order to run it. Otherwise it would be in queued state    

