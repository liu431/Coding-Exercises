## Notes 

Taken from [Udemy class Spark and Python for Big Data with PySpark](https://www.udemy.com/course/spark-and-python-for-big-data-with-pyspark/)

Documentation:
[Spark](https://spark.apache.org/),
[PySpark](https://spark.apache.org/docs/latest/api/python/getting_started/index.html),
[MLlib](https://spark.apache.org/docs/latest/ml-guide.html)

Skills: Spark, PySpark, Spark Streaming, MLlib for Machine Learning, Spark 2.0 DataFrames, DataBricks 

### Spark and Big Data basics
#### Local vs. Distributed
* Local: limited to the cores/computation resoruces on local machine
* Distributed: has access to the computational resoruces across a number of machines connected throigh a network; easily scaling; fault tolerance

#### Hadoop
* A way to distribute very large files across multiple machines
* HDFS: Hadoop Distributed File System
* Allow a user to work with large data sets; duplicate blocks of data for fault tolerance
* MapReduce: allow computation on that data by distributing a computational task to a distributed data set

#### Spark
* Improve on the concepts of using distribution
* A flexible alternative to MapReduce
* Use data stored in Cassandra, AWS S3, HDFS, and more
* Spark vs MapReduce
  - MapReduce requires files to be stored in HDFS, Spark does not
  - Spark can perform operations up to 100x faster than MapReduce
  - MapReduce writes most data to disk after each map and reduce operation; Spark keeps most of the data in memory after each transformation and can spill over to disk if the memory is filled
  - Core idea: Resilient Distributed Dataset (RDD)
    - Distributed collection of data
    - Fault-tolerant
    - Parallel operation - partioned
    - Able to use many data sources
    - Immutable, lazily evaluated, and cacheable
  - Operations
    - Transformations: a receipt to follow
    - Actions: perform what the receipt says to do and return something back 
  - Files are being distributed as RDD; Syntax as DataFrame

### Setting up Spark in various ways
Spark will run on a cluster on a service, like AWS.

4 options:
* Ubuntu + Spark + Python on VirtualBox
* AWS EC2 with Python and Spark
  - EC2: provide resizable compute capacity in the cloud
  - A VM we can access through the internet
  - How to connect: [Connect to your Linux instance from Windows using PuTTY](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html)
  - Host name: ubuntu@DNS_Name; Browse ppk key; Connect
  - Installations on EC2
  
```bash
sudo apt-get update # update everything
clear # clear console
sudo apt install python3-pip # install python
pip3 install jupyter # install jupyter
sudo apt-get install default-jre # install Java
java -version # confirm java instllation
sudo apt-get install scala
scala -version # confirm scala instllation
pip3 install py4j # py4j library
wget http://archive.apache.org/dist/spark/spark-3.2.0/spark-3.2.0-bin-hadoop3.2.tgz # install Spark
sudo tar -zxvf spark-3.2.0-bin-hadoop3.2.tgz # unzip file
ls # list files
cd spark-3.2.0-bin-hadoop3.2/ # change directory
pwd # print working directory (/home/ubuntu/spark-3.2.0-bin-hadoop3.2)
cd # return to home directory
pip3 install findspark # help connect Pythonand Spark
sudo -H pip install jupyter # fix jupyter 
jupyter notebook --generate-config # generate config .py file
mkdir certs # make new dir certs
cd certs # open certs dir
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout mycert.pem -out mycert.pem # create certification
cd ~/.jupyter/
vi jupyter_notebook_config.py
# in vi editor, press 'i' for insert
c = get_config()
c.NotebookApp.certfile = u'/home/ubuntu/certs/mycert.pem'
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888
# type "Esc" and type ":wq!" to quite vi
sudo chmod 777 mycert.pem
cd
jupyter notebook
# Copy the IP address; replace localhost with DNS from AWS
```

* Databricks Notebook System
* AWS EMR Notebook

### Python and Spark 2.0 DataFrames
* Spark DataFrames hold data in a column and row format


### PySpark Project Exercise

### Introduction to Machine Learning

### Linear Regression
 
### Logistic Regression

### Decision Trees and Random Forests

### Gradient Boosted Trees

### K-means Clustering

### Recommender Systems

### Natural Language Processing


### Spark Streaming (Local and Twitter)
