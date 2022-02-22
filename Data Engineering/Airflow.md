## Note on Apache Airflow

[Airflow](https://airflow.apache.org/): an open source platform to programmatically author, schedule and monitor workflows; best orchestrator to run pipelines in the right way at the right order at the right time

[Udemy - Airflow: The Hands-On Guide ](https://www.udemy.com/course/the-ultimate-hands-on-course-to-master-apache-airflow/)

### [Install](https://airflow.apache.org/docs/apache-airflow/stable/start/local.html)

- Open Anaconda Prompt
```bat
SET AIRFLOW_HOME=~/airflow
pip install "apache-airflow==2.2.2" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.2.2/constraints-3.7.txt" --user
```

### Concepts
#### Airflow
* Web sever: Flask server with Gunicorn serving the UI
* Scheduler: Daemon in charge of scheduling workflows
* Metastore: Database where metadata are stored
* Executor: Class defining how your tasks should be executed
* Worker: Process/subprocess executing your task
* DAG: Directed acyclic graph (without loops)
* Operator: Action (execute something); Transfer (transfer data from source to destination); Sensor (wait something to happen)

#### Docker
* Enable user to install and run softwares regardless of the installed dependencies and the operating system used
* Dockerfile -> Docker image -> Container
* Docker compose: Define and run multi-container Docker application





