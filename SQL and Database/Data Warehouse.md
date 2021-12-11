## Notes 

Taken from [Udemy class Data Warehouse Fundamentals for Begineers](https://www.udemy.com/course/data-warehouse-fundamentals-for-beginners/)

### Concepts
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

#### ETL: Extract, Transform, Load

### Architecture
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






