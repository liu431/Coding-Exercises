## Notes 

Taken from [Udemy class Data Warehouse Fundamentals for Begineers](https://www.udemy.com/course/data-warehouse-fundamentals-for-beginners/)

[Tutorialspoint Data Warehousing Tutorial](https://www.tutorialspoint.com/dwh/index.htm)

### Data Warehousing Concepts
#### Value
Data warehousing is the fundemental underpinning of modern data-driven decision making (past, present, future, the unknown).

Bill Inmon (1990): a data warehouse is a subject oriented, integrated, time-variant, and non-volatile collection of data

#### Terminologies
* Metadata: data that are used to represent other data
* Metadata Repository: contains the following metadata (Business, Operational, Data for mapping from operational environment to data warehouse, The algorithms for summarization)
* Data Cube: represent data in multiple dimensions; defined by dimensions and facts
* Data Mart: subset of organization-wide data that is valuable to specific groups of people in an organization
 
#### Process Flow 
* Extract and load the data.
* Cleaning and transforming the data.
* Backup and archive the data.
* Managing queries and directing them to the appropriate data sources.

#### What is a data warehouse

* A warehouse filled with data
* Build on top of some types of databases
* Data are copied from external sources
* Integrated, subject oriented, __time variant__, __non volatile__

#### Compare with other tools
* Data lake is built on top of big data sources.
* Data virtualization is read-only DDBMS (distributed database management system).

### Data Warehousing Architecture

#### Business Analysis Framework
* Top-down view: allows the selection of relevant information needed for a data warehouse.
* Data source view: presents the information being captured, stored, and managed by the operational system.
* Data warehouse view: includes the fact tables and dimension tables. It represents the information stored inside the data warehouse.
* Business query view : view of the data from the viewpoint of the end-user

#### Three-Tier Architecture
* Bottom Tier − the data warehouse database server. It is the relational database system. We use the back end tools and utilities to feed data into the bottom tier by performing the Extract, Clean, Load, and refresh functions.

* Middle Tier − the OLAP Server that can be implemented in either of the following ways.
  - By Relational OLAP (ROLAP): an extended relational database management system; maps the operations on multidimensional data to standard relational operations.
  - By Multidimensional OLAP (MOLAP) model: directly implements the multidimensional data and operations.
* Top-Tier - the front-end client layer; holds the query tools and reporting tools, analysis tools and data mining tools.

#### Online Analytical Processing Server (OLAP) 

* Relational OLAP (ROLAP): uses relational or extended-relational DBMS
List of OLAP operations
  - Roll-up: performs aggregation on a data cube by climbing up a concept hierarchy for a dimension or dimension reduction
  - Drill-down: one or more dimensions from the data cube are added
  - Slice: select one particular dimension from a given cube and provides a new sub-cube
  - Dice: selects two or more dimensions from a given cube and provides a new sub-cube
  - Pivot (rotate): rotates the data axes in view in order to provide an alternative presentation of data
   
* Multidimensional OLAP (MOLAP): uses array-based multidimensional storage engines for multidimensional views of data
* Hybrid OLAP (HOLAP): offers higher scalability of ROLAP and faster computation of MOLAP
* Specialized SQL Servers: provides advanced query language and query processing support for SQL queries over star and snowflake schemas in a read-only environment

#### Centralized Data Warehouse
* Use single database; One stop shopping for data to support business decisions
* Hostorical challenges: technology, work processes
* Today's challenge: organizational & human factors

#### Data Mart
* Smaller scale, narrowly-focused data warehouse
* Two types: dependent and independent (whether it draws data from warehouse or sources)
* Data warehouse vs independent data mart: warehouse has data from many sources; data marts has one or some sources
* Analogy: data marks as retailers; warehouse as wholesaler

#### Component-Based Data Warehouse
* Multiple decomposited components operating together for the data warehouse environment
* Disadv: inconsistent data; difficult to cross-integrate

#### Cube = Multidimentional database (MDBMS)
* Not a relational database
* Specialized "dim-aware" database
* Alterntaive for smaller-scale data warehouse and data marts
* Fast uery response time for "modest" data volumes
* Less flexible data structures than RDBMS

#### ODS (Operational Data Store)
* Integrate current operational data from multiple sources
* Often real-time source -> ODS data feeds -> "What is happening now?"
* Superseded by big data (velocity needs)

#### Staging Layer
* Important part in Extraction as landing zone
* Pull the data as quickly as possible from data sources
* Persistent vs Non-persistent: whether or not delete dat athat are already moved to user layer

### Bring Data Into Data Warehouse - ETL: Extract, Transform, Load
* Extract: quickly pull raw data from source applications; traditionally done in "batches"; land in data warehouse staging layer
* Transform: prepare for __uniform__ data in user access layer
* Load: store uniform data in user access layer

#### ELT
* Load the data before transformation
* "Blast" data into big data environment, such as Hadoop HDFS, AWS S3, etc
* Likely used when building data lake

[Comparison](https://www.xplenty.com/blog/etl-vs-elt/#comparison)

#### Initial loading ETL
* Normally one time only
* Before data warehouse goes live
* All __relevant__ data definitely/probably needed for BI and analytics; not all possible source data

#### Incremental ETL
* Incrementally "refreshes" the data warehouse
* Bring in new and modified data
* Special handling for deleted data
* Keep DW up to data
* 4 patterns
  - Append
  - In-place update
  - Complete replacement
  - Rolling append

#### Data Transformation
* Goal: "Apple to Apple" comparison -> uniformity, restructuring
* Models: 
  - Data value unification of value, type, size
  - De-duplication of same record from different systems
  - Dropping columns (vertical slicing) of unnecessary information
  - Value-based row filtering (horizontal slicing)
  - Correcting known errors

#### Mix-and-Match Incremental ETL
* Frequency of ETL feeds: Daily, Daily, Hourly, Weekly...
* Types of ETL feeds: Append, Replace, Rolling Append...

### Data Warehousing Design: Building Blocks

* BI Category drives data model
  - Basic reporting -> Dimensional
  - Online analytical processing (OLAP) -> Dimensional
  - Predictive analytics -> Data minig/specialized
  - Exploratory analytics -> Data minig/specialized

* Dimensionality (what does the data column measure)
  - One or more measurements (quantifiable; such as average annual salary, max time )
  - Dimensional context of each measurement (__By__(sliced and grouped), __For__(one or more specific values))
 
* Facts, Fact Tables, Dimensions, and Dimension Tables
  - Facts: numeric and quantifiable, measurement/metric
  - Fact table: store facts
  - Dimensions: context of a fact (Ex. department, major, student, employee, building)
  - Dimension Tables: store dimensions

* Additivity in Facts
  - Facts that could be aggregated. Ex. employees' salary, students' credit hours
  - Non-additive facts
    - Ex. GPA, margins, percentages, ratios
    - Possibly store them for individual row easy access 
    - Calculate aggregate averages, ratios, percentages, etc   
  - Semi-additive facts
    - Sometimes could be added; sometimes not  
    - Typically used in periodic snapshot fact tables

* Star Schema vs. Snowflake Schema

| Star | Snowflake |
| --- | ----------- |
| All dimensions along a given hierarchy in one dim table | Each dim/dimensioanl level in its own table |
| Only one level away from fact table along each hierarchy | One or more levels away from fact table along each hierarchy |
| With one fact table visually resembles a star | With one fact table visually resembles a snowflake |
| Overall fewer database joins for drilling up/down | Overall more databases joins for drilling up/down |
| Database primary -> foreign key relationships straightforward | Database primary-> foreign key relationships more complex|
| Typically more database storage needed for dim data | Typically less database storage needed for dim data |
|"Denormalized" dimension table data | "Normalized" dimension table data |

* Database Keys 
  - Primary  vs. foreign keys
    - Primary: unique identifier for each row in a table; could be a column (field)
    - Foreign: some other tables' primary key; used to indicate logical relationship; help improve query performance 
  - Natural vs. surrogant keys
    - Natural: might be "cryptic" or "understandable"; travel from source systems with the rest of the data; keep as "secondary keys"
    - Surrogate (preferred to be used as primary key): no business meaning; generated by the database itself or a supplemenatl system

### Dimensional Modeling (Design Facts, Fact Tables, Dimensions, and Dimension Tables)
* Design Dim Tables
  - Name: Suffix with _DIM, Ex Faculty_DIM
  - Snowflake scheme PK-FK rules
    - 1 table for each level of a hierarchy
    - Every non-terminal dimension has 1. primary/surrogate key; 2. the next highest level's primary/surrogate key as a foreign key

* Fact Tables
  - Transaction: record facts (measurements) from transactions
  - Periodic snapshot: track a given measurement at regular intervals
  - Accumulating snapshot: track the process of a business process through formally defined stages
  - Factless
    - Record occurrence of a transaction that has no measurements
    - Record coverage or eligibility relationships 







































