from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
from random import randint

with DAG("my_dag", 
         start_date = datetime(2021, 1, 1),
         schedule = "@daily",
         description = "Training Machine Learning Models",
         tags = ["data engineering", "YZ"],
         catchup=False) as dag:
    
    @task # decorator
    # function that returns a random accuracy score
    # utilizing dynamic task mapping
    def training_model(accuracy):
        return accuracy
    
    @task.branch # decorator
    def choose_best_model(accuracies):
        best_accuracy = max(accuracies)
        if (best_accuracy > 8):
            return 'accurate'
        else:
            return 'inaccurate'

    accurate = BashOperator(
        task_id = "accurate",
        bash_command = "echo 'accurate'"
    )

    inaccurate = BashOperator(
        task_id = "inaccurate",
        bash_command = "echo 'inaccurate'"
    )

    # dynamic task mapping (create 3 tasks)
    choose_best_model(training_model.expand(accuracy=[5, 10, 6])) >> [accuarte, inaccurate]