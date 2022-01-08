## Notes

[Udemy class - Writing production-ready ETL pipelines in Python / Pandas](https://www.udemy.com/course/writing-production-ready-etl-pipelines-in-python-pandas/)

### Introduction

__Tools__: Python 3.9, Jupyter Notebook, Git and Github, Visual Studio Code, Docker and Docker Hub and the Python packages Pandas, boto3, pyyaml, awscli, jupyter, pylint, moto, coverage and the memory-profiler.

__Best practices__: design principles, clean coding, virtual environments, project/folder setup, configuration, logging, exeption handling, linting, dependency management, performance tuning with profiling, unit testing, integration testing, dockerization

__Project goal__: extract the Xetra dataset from the AWS S3 source bucket on a scheduled basis, create a report using transformations and load the transformed data to another AWS S3 target bucket (format: parquet)

__Production environment__: Code Repo on Github -> Image Repo on Docker -> Orchestration (Argo or Airflow) -> Execution Platform (Kubernete)

__Links to resources__: [Deutsche Börse Public Dataset (DBG PDS)](https://github.com/Deutsche-Boerse/dbg-pds), [Docker Image](https://hub.docker.com/r/schwarzl87/xetra-etl)

### Quick and Dirty Solutions
#### Virtual environment
* Standard libaries: pyvenv, venv
* Third-party libraries: virtualenv, pyenv, pyenv-virtualenv, virtualenvwrapper, pyenv-virtualenvwrapper, __pipenv__

[Python Dev Environment](https://dev.to/bowmanjd/python-dev-environment-part-1-setup-py-venv-and-pip-22gd)

```python
cd C:\Users\lliu9\OneDrive\Data Engineering\Udemy class - ETL Pipelines\xetra_project
pipenv shell --python C:\Users\lliu9\AppData\Local\Programs\Python\Python310\python.exe
```


### Functional Approach


### Object Oriented Approach

### Setup and Class Frame Implementation

### Code Implementation

### Finalizing the ETL job
