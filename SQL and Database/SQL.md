## SQL Notes
### Syntax
Link: [W3 SQL Tutorial](https://www.w3schools.com/sql/)
### Table Joins (combine columns from two or more tables)
* (INNER) JOIN: returns records that have matching values in both tables
* LEFT (OUTER) JOIN: returns all records from the left table, and the matched records from the right table
* RIGHT (OUTER) JOIN: returns all records from the right table, and the matched records from the left table
* FULL (OUTER) JOIN: returns all records when there is a match in either left or right table; Null for unmatched cells
* CROSS JOIN: returns the Cartesian product which is the product of rows of two associated tables

```sql
# SELF JOIN: a regular join, but the table is joined with itself
SELECT column_name(s)
FROM table1 T1, table1 T2
WHERE condition;
## Employee(employee_id,manager_id,join_date); Find all the employees who joined before their manager
SELECT employee_id
FROM Employee E1 
LEFT JOIN Employee E2 ON E1.employee_id = E2.manager_id
WHERE E1.join_date < E2.join_date
```

```sql
# UNION: combine the result-set of two or more SELECT statements; selects only distinct values by default
# UNION ALL: allow duplicate values
SELECT Client FROM MarketA
UNION
SELECT Client FROM MarketA
ORDER BY Client;
```

#### DELETE (delete existing records in a table)
```sql
DELETE FROM tbl WHERE Username = 'Test User'
```

#### WHERE & HAVING
WHERE is applied before GROUP BY, HAVING is applied after (and can filter on aggregates).
A HAVING clause is like a WHERE clause, but applies only to groups as a whole (that is, to the rows in the result set representing groups), whereas the WHERE clause applies to individual rows. [Link](https://docs.microsoft.com/en-us/sql/ssms/visual-db-tools/use-having-and-where-clauses-in-the-same-query-visual-database-tools?view=sql-server-ver15)
_MySQL allows referencing SELECT level aliases in GROUP BY, ORDER BY and HAVING._

##### Ex. [Find Duplicate Values](https://chartio.com/learn/databases/how-to-find-duplicate-values-in-a-sql-table/)
```sql
SELECT a.* 
FROM
(SELECT ID, Name, COUNT(*)
FROM User 
GROUP BY ID, Name
HAVING COUNT(*) > 1) b
JOIN a.ID = b.ID AND a.Name = b.Name
```

### CASE
Go through conditions and return a value when the first condition is met
#### Ex. FInd customer who only order phone
```sql
SELECT CustomerName
FROM 
(SELECT *, SUM(CASE WHEN Product='phone' THEN 1 ELSE 0) AS Phones
FROM Customer
GROUP BY CustomerName) t
WHERE Phones > 0
```

### COALESCE()
Return the first non-null value in a list

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

##### Ex. Given salary(department_id,employee_id,salary), list all employees with salary greater than the average department salary and also greather than $50K
```sql
SELECT employee_id
FROM 
(SELECT *, AVG(SALARY) OVER (PARTITION BY department_id) AS depart_avg
FROM salary) S
WHERE salary > 50000
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

#### Pivot — Rows to Columns; allow you to display row values as columns
MySQL does not have PIVOT function; use a CASE expression along with an aggregate function
[PIVOT and UNPIVOT in SQL Server] (https://docs.microsoft.com/en-us/sql/t-sql/queries/from-using-pivot-and-unpivot?view=sql-server-ver15)
##### Ex. Get results of each client's order numbers in different month
```sql
SELECT ClientName,  
SUM(MONTH(Order) = 'January') AS Order_Jan,
SUM(MONTH(Order) = 'February') AS Order_Feb
...
FROM table
GROUP BY ClientName
```

##### Ex. Given Monthly_Revenue (company_name,month,revenue), Write a query to pull the monthly revenue as columns instead of rows.
```sql
SELECT company_name,
# Using CASE WHEN
SUM(CASE WHEN (month='January') THEN revenue ELSE NULL END) AS January
# Using IF
SUM(IF(month='January', revenue, NULL)) AS January
...
FROM Monthly_Revenue
GROUP BY company_name
```

```sql
# PIVOT in SQL Server
SELECT company_name, [January], [February], [March], [April], [May], [June], [July], [August], [September], [October], [November], [December]
FROM Monthly_Revenue
PIVOT(
SUM(revenue) FOR month IN ([January], [February], [March], [April], [May], [June], [July], [August], [September], [October], [November], [December])
) as PivotTable
```







