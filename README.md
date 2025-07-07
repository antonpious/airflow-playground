# airflow-playground
Showcase Airflow features


# install airflow in standalone mode in a folder in your local computer
follow the instructions present [here](https://airflow.apache.org/docs/apache-airflow/stable/start.html)   

## copy the file to the dag folder

`cp tutorial.py /Users/anton/Software/airflow/dags`

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



