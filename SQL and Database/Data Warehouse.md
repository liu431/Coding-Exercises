## Notes 

Taken from [Udemy class Data Warehouse Fundamentals for Begineers](https://www.udemy.com/course/data-warehouse-fundamentals-for-beginners/)

### Data Warehousing Concepts
#### Value
Data warehousing is the fundemental underpinning of modern data-driven decision making (past, present, future, the unknown).

#### What is a data warehouse

* A warehouse filled with data
* Build on top of some types of databases
* Data are copied from external sources
* Integrated, subject oriented, __time variant__, __non volatile__

#### Compare with other tools
* Data lake is built on top of big data sources.
* Data virtualization is read-only DDBMS (distributed database management system).

### Data Warehousing Architecture
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







































