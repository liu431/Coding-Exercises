### [Relational vs Non-Relational Databases](https://realpython.com/data-engineer-interview-questions-python/#questions-on-design-patterns-and-etl-concepts)
||Relational|Non-relation|
|-|-|-|
|Vendors|MySQL, PostgreSQL, SQL Server, SQLite|MongoDB, DynamoDB|
|Schema|Each table has a schema, which is the columns and types a record is required to have. Each schema must have at least one primary key that uniquely identifies that record.|Inherently schema-less; nested structure|
|Change|A change in a schema must be applied to all records. This can sometimes cause breakages and big headaches during migrations.|Records can still have primary keys, but a change in the schema is done on an entry-by-entry basis. More suitable when there is constantly changing schema.|
|Scalability|Difficult to distribute|Easier as a collection of related records can be easily stored on a particular node|

* Other types
  - Elastic Search: for text search; leverages its document-based database to create a powerful search tool.
  - Redis (Cache Databases): hold frequently accessed data; alleviate load and serve requests faster; reside in memory

### [Producer-Consumer pattern](https://realpython.com/data-engineer-interview-questions-python/#questions-on-design-patterns-and-etl-concepts)
A worker (the Producer) produces data of some kind and outputs it to a pipeline. This pipeline can take many forms, including network messages and triggers. After the Producer outputs the data, the Consumer consumes and makes use of it. These workers typically work in an asynchronous manner and are executed in separate processes.

In big data, the mapper can be seen as the Producer, while the reducer is effectively the Consumer.

### [Normalization](https://www.guru99.com/database-normalization.html)
Purpose: eliminate redundant (repetitive) data and ensure data is stored logically
* 1NF (First Normal Form): each table cell should contain a single value; each record needs to be unique
* 2NF (Second Normal Form): single column primary key that does not functionally dependant on any subset of candidate key relation
* 3NF (Third Normal Form): has no transitive functional dependencies (when changing a non-key column, might cause any of the other non-key columns to change)
* BCNF (Boyce-Codd Normal Form): 3NF and not have any dependency between two non-prime attributes
* 4NF (Fourth Normal Form): no database table instance contains two or more, independent and multivalued data describing the relevant entity
* 5NF (Fifth Normal Form): cannot be decomposed into any number of smaller tables without loss of data


### Schemas
[Snowflake vs Star](https://www.xplenty.com/blog/snowflake-schemas-vs-star-schemas-what-are-they-and-how-are-they-different/)
* Star: contains the Fact Tables and the Dimension Tables; top-down model
* Snowflake: contains the Fact Tables, Dimension Tables, and the Sub-Dimension Tables; bottom-up model

#### Primary key
* A single column value used to identify a database record uniquely
* Cannot be null; given a value when new record is inserted

#### [Foreign keys](https://dev.mysql.com/doc/mysql-tutorial-excerpt/8.0/en/example-foreign-keys.html)
* Permit cross-referencing related data across tables
* Ensure rows in one table have corresponding rows in another
* Can be null
* Referential integrity: only be able to insert values into your foreign key that exist in the unique key in the parent table

#### [DDL, DQL, DML, DCL and TCL](https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/)
* DDL – Data Definition Language; define the database schema
* DQl – Data Query Language; get the data out of the database to perform operations with it (SELECT)
* DML – Data Manipulation Language; includes: INSERT, UPDATE, DELETE, LOCK
* DCL – Data Control Language; deal with the rights, permissions, and other controls of the database system
* TCL - Transaction Control Language; deal with the transaction within the database

### OLTP and OLAP 
[Source](https://techdifferences.com/difference-between-oltp-and-olap.html)

OLTP and OLAP both are the online processing systems. OLTP is a transactional processing while OLAP is an analytical processing system. OLTP is a system that manages transaction-oriented applications on the internet for example, ATM. OLAP is an online system that reports to multidimensional analytical queries like financial reporting, forecasting, etc.
* Main operations
  - OLTP: insert, update and delete 
  - OLAP: extract multidimensional data for analysis.


### Query optimization vs Database performance tuning
[Source](https://www.solarwinds.com/database-performance-analyzer/use-cases/database-performance-tuning)

SQL performance tuning is narrower in scope than database performance tuning. 

SQL performance tuning refers to best practices and procedures designed to ensure relational databases are running as efficiently as possible. This primarily involves tuning, managing, and optimizing SQL queries and indexes.

#### Techniques

Factors: Joins, Aggregations, Traversals, Records

[Example 1](https://beginner-sql-tutorial.com/sql-query-tuning.htm)
* Use the actual columns names in SELECT statement instead of than '*'
* Do not use HAVING clause for any other purposes than filtering
* Try to minimize the number of subquery block in your query
* EXISTS is efficient when most of the filter criteria is in the main query
* Use EXISTS instead of DISTINCT when using joins which involves tables having one-to-many relationship
* Use UNION ALL in place of UNION
* Reducing table size - filter data to include only the observations you need
* Making joins less complicated - reduce table sizes before joining them


### [Clustered and nonclustered indexes](https://www.guru99.com/clustered-vs-non-clustered-index.html)
Cluster index is a type of index that sorts the data rows in the table on their key values whereas the Non-clustered index stores the data at one location and indices at another location.

### Data Models

##### Ex. Can you give me a data model which will help answer the following questions. No SQL queries just the data model. (*Amazon BIE*)
a. Top grossing movie last year?

b. All movies which starred Brad Pitt.

c. Every actor which Bradd Pitt has worked with.

d. Top Movies (star rating) for 2019?

Ans:

Movies
- Movie ID
- Movie Name
- Movie Year
- Movie Box Office Results
- Star Ratings

Actor and Actress
- ID
- Name
- Movie ID

### Database Management
[Create View](https://dev.mysql.com/doc/refman/8.0/en/create-view.html)

Redunant data

Database view

Stored procedure

[Stored routines](https://zetcode.com/mysql/routines/)

[With rollup](https://mariadb.com/kb/en/select-with-rollup/)

[View Processing Algorithms](https://dev.mysql.com/doc/refman/8.0/en/view-algorithms.html#:~:text=The%20optional%20ALGORITHM%20clause%20for,MERGE%20%2C%20TEMPTABLE%20%2C%20or%20UNDEFINED%20.)
