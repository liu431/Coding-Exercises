#### OLTP and OLAP 
[Source](https://techdifferences.com/difference-between-oltp-and-olap.html)

OLTP and OLAP both are the online processing systems. OLTP is a transactional processing while OLAP is an analytical processing system. OLTP is a system that manages transaction-oriented applications on the internet for example, ATM. OLAP is an online system that reports to multidimensional analytical queries like financial reporting, forecasting, etc.

OLTP’s main operations are insert, update and delete whereas, OLAP’s main operation is to extract multidimensional data for analysis.


#### Query optimization vs performance tuning

#### Techniques
[Example 1](https://beginner-sql-tutorial.com/sql-query-tuning.htm)
* Use the actual columns names in SELECT statement instead of than '*'
* Do not use HAVING clause for any other purposes than filtering
* Try to minimize the number of subquery block in your query
* EXISTS is efficient when most of the filter criteria is in the main query
* Use EXISTS instead of DISTINCT when using joins which involves tables having one-to-many relationship
* Use UNION ALL in place of UNION
