from airflow.models import DAG
from airflow.sensors.filesystem import FileSensor
from datetime import datetime

with DAG(
    "dag_sensor",
    schedule_interval="@daily",
    start_date = datetime(2024, 1, 1),
    description = "using sensors to trigger DAGs",
    tags = ["data engineering", "sensors", "YZ"],
    catchup = False ) as dag:
    
    waiting_for_file = FileSensor(
        task_id = "waiting_for_file",
        poke_interval = 30, # check if file exists at a specific location every 30s
        timeout = 60 * 5, # 60 sec * 5 = 5 mins, prevents deadlock
        mode = "reschedule", # Best practice knowning workers will run for > 10 mins
        soft_fail = True # if sensor is longer to execute than timeout, then skip the sensor
    )

# types of sensors:
# The FileSensor: Waits for a file or folder to land in a filesystem.
# The S3KeySensor: Waits for a key to be present in a S3 bucket.
# The SqlSensor: Runs a sql statement repeatedly until a criteria is met.
# The HivePartitionSensor: Waits for a partition to show up in Hive.
# The ExternalTaskSensor: Waits for a different DAG or a task in a different DAG to complete for a specific execution date.