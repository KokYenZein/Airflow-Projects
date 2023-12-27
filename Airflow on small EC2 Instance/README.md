# Installing and Running Airflow on a small EC2 Instance
This project aims to install and run airflow on a EC2 Instance that has a minimum requirement of 2GB of RAM (due to Postgresql)


## Steps
- [AWS EC2](#AWS-EC2)
- [Commands](#Commands)
- [Results](#Results)

## AWS EC2

1. Once logging into AWS, access EC2 and Launch an Ubuntu instance with at least t2.small
2. Once launched, head to Security > Security Groups > Edit inbound rules to add a rule with Custom TCP Type with 8080 Port range
3. Save rules, then connect to the instance

## Commands
1. Once you are in your EC2 Instance command line, follow the following commands:
```
sudo apt update
```

## Results
- At the end you should be able to access your public IPV4 web address adding a ":8080" to access your local airflow
- For Example, "ec2-3-86-233-186.compute-1.amazonaws.com:8080" to which enter "airflow" as username and password
- At last you should get:
![airflow webpage.png](https://github.com/KokYenZein/Airflow-Projects/Airflow on small EC2 Instance/airflow webpage.png?raw=true)
