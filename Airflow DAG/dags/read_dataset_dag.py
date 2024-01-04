from airflow import DAG, Dataset
from airflow.decorators import task
from datetime import datetime

my_file = Dataset("tmp/my_file.txt")

with DAG(
    "read_dag_dataset",
    schedule_interval = [my_file],
    start_date = datetime(2024, 1, 1),
    description = "activating airflow dags with datasets",
    tags = ["data engineering", "dataset", "YZ"],
    catchup = False) as dag:

    @task
    def read_my_file():
        with open(my_file.uri, "r") as f:
            print(f.read())

    read_my_file()
