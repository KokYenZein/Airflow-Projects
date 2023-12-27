# Installing and Running Airflow on a small EC2 Instance
This project aims to install and run airflow on a EC2 Instance that has a minimum requirement of 2GB of RAM (due to Postgresql)


## Steps
- [AWS EC2](#Introduction)
- [Commands](#project-details)
- [Results](#results)

## AWS EC2

1. Once logging into AWS, access EC2 and Launch an Ubuntu instance with at least t2.small
2. Once launched, head to Security > Security Groups > Edit inbound rules to add a rule with Custom TCP Type with 8080 Port range
3. Save rules, then connect to the instance

## Commands
1. Once you are in your EC2 Instance command line, follow the following commands:
```
sudo apt update

sudo apt install python3-pip

sudo apt install sqlite3
```

2. We then want to create a virtual environment
```
sudo apt install python3.10-venv

python3 -m venv ec2venv

source ec2venv/bin/activate

sudo apt-get install libpq-dev
```

3. Install Apache Airflow
```
pip install "apache-airflow[postgres]==2.5.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.0/constraints-3.7.txt"

airflow db init
```

4. Install and configure postgresql
```
sudo apt-get install postgresql postgresql-contrib

sudo -i -u postgres

psql

CREATE DATABASE airflow;
CREATE USER airflow WITH PASSWORD 'airflow';
GRANT ALL PRIVILEGES ON DATABASE airflow TO airflow;
```
Then hit CTRL-D twice to exit back to the virtual environment

5. Connect to airflow to configure airflow to connect to postgre and initialize users
```
cd airflow

sed -i 's#SequentialExecutor#LocalExecutor#g' airflow.cfg

airflow db init

airflow users create -u airflow -f airflow -l airflow -r Admin -e airflow@gmail.com
```

6. Finally connect to airflow
```
airflow webserver &

airflow scheduler
```

## Results
- At the end you should be able to access your public IPV4 web address adding a ":8080" to access your local airflow
- For Example, "ec2-3-86-233-186.compute-1.amazonaws.com:8080" to which enter "airflow" as username and password
- At last you should get:
![airflow webpage.png](https://github.com/KokYenZein/Airflow-Projects/blob/main/Airflow%20on%20small%20EC2%20Instance/airflow%20webpage.png)