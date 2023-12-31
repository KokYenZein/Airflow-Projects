from airflow import DAG
from airflow.decorators import task
from datetime import datetime
from include.datasets import MY_FILE

with DAG(
    "write_dag_dataset",
    schedule_interval = "@daily",
    start_date = datetime(2024, 1, 1),
    description = "activating airflow dags with datasets",
    tags = ["data engineering", "dataset", "YZ"],
    catchup = False) as dag:

    @task(outlets=[MY_FILE])
    def update_file():
        with open(MY_FILE.uri, "a+") as f:  # this opens a file speciifc by the uri in append mode ("a+")
            f.write("producer update")  # if the file does not exist, it will be created ("a+")
    
    update_file()