## SQL Notes
### Syntax
Link: [W3 SQL Tutorial](https://www.w3schools.com/sql/)
### Table Joins (combine rows from two or more tables)
* (INNER) JOIN: returns records that have matching values in both tables
* LEFT (OUTER) JOIN: returns all records from the left table, and the matched records from the right table
* RIGHT (OUTER) JOIN: returns all records from the right table, and the matched records from the left table
* FULL (OUTER) JOIN: returns all records when there is a match in either left or right table; Null for unmatched cells

```sql
# SELF JOIN: is a regular join, but the table is joined with itself
SELECT column_name(s)
FROM table1 T1, table1 T2
WHERE condition;
```

#### DELETE (delete existing records in a table)
```sql
DELETE FROM tbl WHERE Username = 'Test User'
```

#### WHERE & HAVING
WHERE is applied before GROUP BY, HAVING is applied after (and can filter on aggregates).
A HAVING clause is like a WHERE clause, but applies only to groups as a whole (that is, to the rows in the result set representing groups), whereas the WHERE clause applies to individual rows. [Link](https://docs.microsoft.com/en-us/sql/ssms/visual-db-tools/use-having-and-where-clauses-in-the-same-query-visual-database-tools?view=sql-server-ver15)
_MySQL allows referencing SELECT level aliases in GROUP BY, ORDER BY and HAVING._

### Date functions
```sql
MONTH(date) # Return the month part of a date
DAY(date) or DAYOFMONTH(date) # Return the day of the month for a date, 'mon'
DAYOFWEEK(date) # Return the weekday index for a date; Sunday is 1
DATEDIFF(date1, date2) # Return number of days between (date1 - date2)
DATE_FORMAT(date, "%Y-%m") # Return the date as Year-Month
```

### Windows function
#### Rank()
* dense_rank(): assign rank to each row within a partition without gaps
* rank(): assign rank to each row within a partition with gaps
* percent_rank():returns the percentile rank of a row within a partition that ranges from 0 to 1

```sql
SELECT product_id, year, RANK() OVER (PARTITION BY product_id ORDER BY year) AS 'rank' 
FROM Sales;
```
#### Nonaggregate functions
* [LAG()](https://www.mysqltutorial.org/mysql-window-functions/mysql-lag-function/): get value from row that precedes the current row (before)
* LEAD(): get value from row that succeeds the current row (after)
```sql
SELECT price, price - LAG(price, 1) OVER () AS price_diff
FROM Orders
```

#### Aggregate functions
* COUNT(): return the number of rows that matches a specified criterion.
* AVG(): return the average value of a numeric column
* SUM(): return the total sum of a numeric column


```sql
# Count cells that satisfy a condition
COUNT(CASE WHEN <condition> THEN 1 END)
```

### Conditions
#### WHERE
EXISTS:test for the existence of any record in a subquery; return TRUE if the subquery returns one or more records
```sql
# Ex: FInd clients who have purchased products over $100
SELECT ClientName
FROM Client
WHERE EXISTS (SELECT ProductName FROM Products WHERE Products.ClientName = Suppliers.ClientName AND Price > 100)
```

### CTE (Common Table Expressions)
#### Recursive CTE (having a subquery that refers to its own name)
```sql
WITH RECURSIVE cte (n) AS
(
  SELECT 1
  UNION ALL
  SELECT n + 1 FROM cte WHERE n < 5
)
SELECT * FROM cte;

# Result table
+------+
| n    |
+------+
|    1 |
|    2 |
|    3 |
|    4 |
|    5 |
+------+
```

#### Multiple CTEs
```sql
WITH cte1 AS
(SELECT * FROM ...),
cte2 as
(SELECT * FROM ...),
cte3 as
(SELECT * FROM ... INNER JOIN cte2 ON...),
SELECT *
FROM cte1
JOIN cte3 ON ...
```

#### [Combine strings under same group](https://stackoverflow.com/questions/31211506/how-stuff-and-for-xml-path-work-in-sql-server)
```sql
SELECT ID,  AllNames = STUFF(
  (SELECT ',' + name FROM temp1 t1 WHERE t1.id = t2.id
  FOR XML PATH ('')), 1, 1, '') 
FROM temp1 t2
GROUP BY ID;
```
#### Fix date
```sql
# Swap day and month (in SQL Server)
UPDATE TALE 
SET Date = 
  DATEFROMPARTS(
    DATEPART(year, [Date]),
    DATEPART(day, [Date]),  
    DATEPART(month, [Date]))
WHERE ...
```

### Pratical Examples
#### [Find outliers](https://dataschool.com/how-to-teach-people-sql/how-to-find-outliers-with-sql/)
##### Order by
Sort the relevant values in both ascending and descending order
##### NTILES()
Separate our data into the same number of groups as the value inside the brackets

#### Pivot — Rows to Columns
MySQL does not have PIVOT function; use a CASE expression along with an aggregate function
```sql
# Get results of each client's order numbers in different month
SELECT ClientName,  
SUM(MONTH(Order) = 'January')AS Order_Jan,
SUM(MONTH(Order) = 'February')AS Order_Feb
...
FROM table
GROUP BY ClientName
```

