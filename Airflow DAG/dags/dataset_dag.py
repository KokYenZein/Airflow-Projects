from airflow import DAG, Dataset
from airflow.decorators import task
from datetime import datetime

my_file = Dataset("tmp/my_file.txt")

with DAG(
    "write_dag_dataset",
    schedule_interval = "@daily",
    start_date = datetime(2024, 1, 1),
    description = "activating airflow dags with datasets",
    tags = ["data engineering", "dataset", "YZ"],
    catchup = False) as dag:

    @task(outlets=[my_file])
    def update_file():
        with open(my_file.uri, "a+") as f:  # this opens a file speciifc by the uri in append mode ("a+")
            f.write("producer update")  # if the file does not exist, it will be created ("a+")
    
    update_file()