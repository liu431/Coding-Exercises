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

[Differences](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe),
[Python Dev Environment](https://dev.to/bowmanjd/python-dev-environment-part-1-setup-py-venv-and-pip-22gd)

```command
# Change to project dir
cd C:\Users\lliu9\OneDrive\Data Engineering\Udemy class - ETL Pipelines\xetra_project
# Create virtial environment of Python 3.10
pipenv shell --python C:\Users\lliu9\AppData\Local\Programs\Python\Python310\python.exe
# List of installed packages
pip list
# Virtual environment location
pipenv --venv
# Install packages
pipenv install pandas
pipenv install awscli
pipenv install jupyter
pipenv install boto3
pipenv install pyarrow
# Launch virtual environment
pipenv shell
# AWS S3 location - check data access
aws s3 ls deutsche-boerse-xetra-pds/2021-04-21 --recursive --no-sign-request
# Launch jupyter notebook
jupyter notebook
```

### Software Testing
* Unit: test individual unit or component
* Integration: test whether independently-developed units or software work correctly when they connect to each other
* System: conducted on a complete, integrated system
* Acceptance: determine whether the requirement is met


### Functional Approach
* Structure the code in small chunks as functions
* Output of a function only relies on teh given input arguments
* Modular and clean code
* Adv: efficiency, lazy evaluation, nested functions, bug-free code, parallel programming


### Object Oriented Approach
* Use objects represent things: attributes contain data; methods manipulate attributes
* 4 primary principles
  * Encapsulation: separation between attributes and methods summarized in one object containing attributes and methods; attributes are not accessible by other objects; for manipulating and communciating with the objects, there are methods callable by other objects
  * Abstration: objects are implemented in a way that other objects should not know their inner details in order to use it and can just use the interface of it
  * Inheritance: ability to create parent and child classes; child class inherits attribues and methods from parent class
  * Polymorphism: each class can use exactly the same methods as its parent class, but method for each child could also be implemented individually



### Setup and Class Frame Implementation

### Code Implementation

### Finalizing the ETL job
