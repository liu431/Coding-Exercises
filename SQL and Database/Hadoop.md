### Note from Udemy Class [The Ultimate Hands-On Hadoop: Tame your Big Data!](https://www.udemy.com/course/the-ultimate-hands-on-hadoop-tame-your-big-data/)

***Tech: MapReduce, HDFS, Pig, Spark, Flink, Hive, HBase, MongoDB, Cassandra, Kafka...***

#### Set up
Download Hortonworks Sandbox (v2.6.5): https://www.cloudera.com/downloads/hortonworks-sandbox/hdp.html
Install VirtualBox: https://www.virtualbox.org/wiki/Downloads

Download sample movie rating data: ml-100k.zip at https://grouplens.org/datasets/movielens/

Initiate Hortonworks Sandbox Session: http://127.0.0.1:8888/

Sign in to Ambari with Username and Password: maria_dev

Hadoop definition by Hortonworks: an open source software platform for distributed processing of very large data sets on computer clusters built from commodity hardware.

#### World of Hadoop
###### Core Hadoop Ecosystem
* HDFS (Hadoop Distributed File System): distributed data storage that keep redundant copies of the data to backup
* YARN (Yet Another Resource Negotiator): manage resources on the computing cluster, such as what gets to run tasks when, what nodes are available for extra work, etc.
* MapReduce: programming model that process data in the entire cluster; contain mapper and reducer scripts; mapper: transform data in parallel across entire cluster in an efficient manner; reducer: aggregate data together
* Pig: high-level programming API that allow user to write scripts that run MapReduce with langauge like SQL, instead of Python or Java
* Hive: like a SQL database; allow user to execute queries on data stored in the Haddop file system
* Apache Ambari: overview of the cluster resources
* MESOS: Alternative to YARN
* Spark: run with Python, Java, or Scala; fast, efficient, versatile
* TEZ: used in conjuction with Hivae to accelerate
* HBase: expose the data on the cluster to transactional platform; NoSQL database
* Storm: process streaming data in real time
* Oozie: way to schedule job on the cluster
* Zookeeper: coordinate everything on the cluster
* Data Ingestion
    * Sqoop: connector between Hadoop database to relational database
    * Flume: transport web logs to the cluster
    * Kafka: collect data from clusters of PCs and broadcast to Hadoop clusters
  
###### External Data Storage
* Relational databases: MySQL, PostgreSQL, SQL Server, etc
* Column-based NoSQL databases: Cassandra, MongoDB, etc.

###### Query Engines
* Drill: write SQL queries that can be run on NoSQL database
* Hue: create queries that work with Hive, HBase, etc.
* Phoenix: make not SQL Hadoop store look like relational store
* Presto:execute query on entire cluster
* Zeppelin: notebook UI for interacting with clusters






