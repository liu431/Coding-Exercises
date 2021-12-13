#### [DDL, DQL, DML, DCL and TCL](https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/)
* DDL – Data Definition Language; define the database schema
* DQl – Data Query Language; get the data out of the database to perform operations with it (SELECT)
* DML – Data Manipulation Language; includes: INSERT, UPDATE, DELETE, LOCK
* DCL – Data Control Language; deal with the rights, permissions, and other controls of the database system
* TCL - Transaction Control Language; deal with the transaction within the database

#### OLTP and OLAP 
[Source](https://techdifferences.com/difference-between-oltp-and-olap.html)

OLTP and OLAP both are the online processing systems. OLTP is a transactional processing while OLAP is an analytical processing system. OLTP is a system that manages transaction-oriented applications on the internet for example, ATM. OLAP is an online system that reports to multidimensional analytical queries like financial reporting, forecasting, etc.

OLTP’s main operations are insert, update and delete whereas, OLAP’s main operation is to extract multidimensional data for analysis.


#### Query optimization vs Database performance tuning
[Source](https://www.solarwinds.com/database-performance-analyzer/use-cases/database-performance-tuning)

SQL performance tuning is narrower in scope than database performance tuning. 

SQL performance tuning refers to best practices and procedures designed to ensure relational databases are running as efficiently as possible. This primarily involves tuning, managing, and optimizing SQL queries and indexes.

#### Techniques
[Example 1](https://beginner-sql-tutorial.com/sql-query-tuning.htm)
* Use the actual columns names in SELECT statement instead of than '*'
* Do not use HAVING clause for any other purposes than filtering
* Try to minimize the number of subquery block in your query
* EXISTS is efficient when most of the filter criteria is in the main query
* Use EXISTS instead of DISTINCT when using joins which involves tables having one-to-many relationship
* Use UNION ALL in place of UNION

#### [Clustered and nonclustered indexes](https://www.guru99.com/clustered-vs-non-clustered-index.html)
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
