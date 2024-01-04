from airflow import DAG
from airflow.decorators import task
from datetime import datetime
from include.datasets import MY_FILE

with DAG(
    "read_dag_dataset",
    schedule_interval = [MY_FILE],
    start_date = datetime(2024, 1, 1),
    description = "activating airflow dags with datasets",
    tags = ["data engineering", "dataset", "YZ"],
    catchup = False) as dag:

    @task
    def read_my_file():
        with open(MY_FILE.uri, "r") as f:
            print(f.read())

    read_my_file()
