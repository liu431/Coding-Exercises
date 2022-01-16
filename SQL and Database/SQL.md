## SQL Notes
Links: 
[W3 SQL Tutorial](https://www.w3schools.com/sql/)

[Model Advanced SQL](https://mode.com/sql-tutorial/intro-to-advanced-sql/)

### Table Joins (combine columns from two or more tables)
* (INNER) JOIN: returns records that have matching values in both tables
* LEFT (OUTER) JOIN: returns all records from the left table, and the matched records from the right table
* RIGHT (OUTER) JOIN: returns all records from the right table, and the matched records from the left table
* FULL (OUTER) JOIN: returns all records when there is a match in either left or right table; Null for unmatched cells
* CROSS JOIN: returns the Cartesian product which is the product of rows of two associated tables
![](https://i2.wp.com/www.datascienceexamples.com/wp-content/uploads/2019/12/join_types.png?fit=1280%2C1200&ssl=1)

#### SELF JOIN: a regular join, but the table is joined with itself
```sql
SELECT column_name(s)
FROM table1 T1, table1 T2
WHERE condition;
```
##### Ex. Find all the employees who joined before their manager
```sql
# Table Employee(employee_id,manager_id,join_date);
SELECT employee_id
FROM Employee E1 
LEFT JOIN Employee E2 ON E1.employee_id = E2.manager_id
WHERE E1.join_date < E2.join_date
```

##### Ex. (Leetcode 1459) Rectangles Area
```sql
SELECT P1.id AS p1, P2.id AS p2, ABS((P1.x_value - P2.x_value) * (P1.y_value - P2.y_value)) AS area
FROM Points P1
JOIN Points P2 ON P1.id < P2.id AND P1.x_value != P2.x_value AND P1.y_value != P2.y_value
ORDER BY area DESC, p1, p2
```

#### UNION: combine the result-set of two or more SELECT statements; selects only distinct values by default
```sql
# UNION ALL: allow duplicate values
SELECT Client FROM MarketA
UNION
SELECT Client FROM MarketA
ORDER BY Client;
```
#### SQL Joins with On or Using

Using: shorthand for the situation where the column names are the same

##### Ex. (Leetcdoe 1677) Product's Worth Over Invoices
```sql
SELECT name, 
IFNULL(SUM(rest), 0) AS rest, IFNULL(SUM(paid), 0) AS paid, 
IFNULL(SUM(canceled), 0) AS canceled, IFNULL(SUM(refunded), 0) AS refunded
FROM Product
LEFT JOIN Invoice USING(product_id)
GROUP BY name
ORDER BY name
```

### Edit Data
#### DELETE (delete existing records in a table)
```sql
DELETE FROM tbl WHERE Username = 'Test User'
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

### Filter Data
#### WHERE & HAVING
WHERE is applied before GROUP BY, HAVING is applied after (and can filter on aggregates).
A HAVING clause is like a WHERE clause, but applies only to groups as a whole (that is, to the rows in the result set representing groups), whereas the WHERE clause applies to individual rows. [Link](https://docs.microsoft.com/en-us/sql/ssms/visual-db-tools/use-having-and-where-clauses-in-the-same-query-visual-database-tools?view=sql-server-ver15)
_MySQL allows referencing SELECT level aliases in GROUP BY, ORDER BY and HAVING._

#### [IN, ANY and ALL](https://stackoverflow.com/questions/3699356/difference-between-in-and-any-operators-in-sql/22779071)
Perform a comparison between a single column value and a range of other values.
* IN (): equals to anything in the List
* ANY(): compare value to each value returned by the subquery
  - < ANY: less than the maximum value in the list
  - > ANY: more than the minimum value in the list
  - = ANY: equivalent to In operator
* ALL(): compare value To every value returned by the subquery

#### EXISTS: test for the existence of any record in a subquery; return TRUE if the subquery returns one or more records
##### Ex. Find clients who have purchased products over $100
```sql
SELECT ClientName
FROM Client
WHERE EXISTS (SELECT ProductName FROM Products WHERE Products.ClientName = Suppliers.ClientName AND Price > 100)
```

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

#### CASE
Go through conditions and return a value when the first condition is met
#### Use CASE and SUM together to get counts 
##### Ex. Find customer who only order phone
```sql
SELECT CustomerName
FROM 
(SELECT *, SUM(CASE WHEN Product='phone' THEN 1 ELSE 0 END) AS Phones
FROM Customer
GROUP BY CustomerName) t
WHERE Phones > 0
```

#### COALESCE()
Return the first non-null value in a list

COALESCE() vs. ISNULL()
* COALESCE translates to CASE expression and ISNULL is a built-in implemented in the database engine.
* COALESCE() can have multiple inputs and it will evaluate in order until one of them is not null such as COALESCE(Col1, Col2, Col3, 'N/A')

### Transform Data

#### Change data types
* CAST(column_name AS integer)
* column_name::integer

#### Strings

* [SUBSTRING(string, start, length)](https://www.w3schools.com/sql/func_mysql_substring.asp): extract a substring from a string
* [LENGTH()](https://www.w3schools.com/sql/func_mysql_length.asp): return the length of the string
* LEFT(string, number of characters): pull a certain number of characters from the left side of a string 
* RIGHT(string, number of characters): pull a certain number of characters from the right side of a string 
* TRIM(both '()' FROM col): remove '(' and ')' from both 'leading' and 'trailing' from the string col
* POSITION('A' IN col) OR STRPOS(col, 'A'): returns a numerical value equal to the character number (counting from left) where that substring first appears in the target string; similar to s.index('A') + 1 in Python 
* SUBSTR(*string*, *starting character position*, *# of characters*): start in the middle of a string
* CONCAT(col1, '', col2) or (col1 || ' ' || col2): combine strings from several columns together (and with hard-coded values)

##### Ex. (Leetcode 1667) Fix the names so that only the first character is uppercase and the rest are lowercase
```sql
SELECT user_id, CONCAT(UPPER(LEFT(name,1)), LOWER(SUBSTRING(name, 2))) AS name
FROM Users
ORDER BY user_id
```

#### Date functions
[DATE_FORMAT](https://www.w3schools.com/sql/func_mysql_date_format.asp)
* DATE_FORMAT(date, "%Y-%m") # Return the date as Year-Month; m: month number; M: English word of the month 
* DATE_FORMAT(day, "%W, %M %e, %Y") # "day_name, month_name day, year" Ex.  Tuesday, April 12, 2022

* YEAR(date) # Return the year part of a date
* MONTH(date) # Return the month part of a date
* DAY(date) or DAYOFMONTH(date) # Return the day of the month for a date, 'mon'
* DAYOFWEEK(date) # Return the weekday index for a date; Sunday is 1
* DATEDIFF(date1, date2) # Return number of days between (date1 - date2)
* NOW() # Get current time as "YYYY-MM-DD HH-MM-SS" (string)
* [DATE_TRUNC('[interval]', time_column)](https://mode.com/blog/date-trunc-sql-timestamp-function-count-on/)
* [TIMESTAMPDIFF(unit, firstdate, seconddate)](https://www.w3resource.com/mysql/date-and-time-functions/mysql-timestampdiff-function.php): returns a value after subtracting a datetime expression from another
* [PERIOD_DIFF()](https://www.w3schools.com/sql/func_mysql_period_diff.asp): returns the difference between two periods. The result will be in months.




### [Windows](https://mode.com/sql-tutorial/sql-window-functions/)
Def:  performs a calculation across a set of table rows that are somehow related to the current row; the rows retain their separate identities

_OVER()_: designates it as a window function

_PARTITION BY_: narrow the window from the entire dataset to individual groups

#### Window alias
Purpose: avoid rewriting same window functions several times

Syntax: WINDOWS _name_ AS (PARTITION BY _var1_ ORDER BY _var2_); come after the WHERE clause

```sql
SELECT State, ClientValue, NTILE(4) OVER ntile_window AS quartile, NTILE(100) OVER ntile_window AS percentile
FROM tbl
WINDOWS ntile_window AS (PARTITION BY State ORDER BY ClientValue)
ORDER BY State, ClientValue
```

#### Ranking function
* DENSE_RANK(): assign rank to each row within a partition without gaps. Ex. 1,1,2
* RANK(): assign rank to each row within a partition with gaps. Ex. 1,1,3
* PERCENT_RANK(): returns the percentile rank of a row within a partition that ranges from 0 to 1
* NTILE(*# of buckets*): identify what percentile (or quartile, or any other subdivision) a given row falls into

##### Ex. Find years when products were first sold 
```sql
SELECT product_id, year
FROM (SELECT product_id, year, RANK() OVER (PARTITION BY product_id ORDER BY year) AS 'rank' 
FROM Sales) t
WHERE rank = 1;
```

#### Nonaggregate functions
* [LAG(column_name,context,default_value)](https://www.mysqltutorial.org/mysql-window-functions/mysql-lag-function/): get value from row that precedes the current row (before)
* LEAD(column_name,context,default_value): get value from row that succeeds the current row (after)
- column name: where you want to check the next/previous row in a column
- context: how many rows you would like to check 
- default_value: value if there is no value present after the last date or before the first date


##### Ex. (Leetcode 180) Find all numbers that appear at least three times consecutively
```sql
# Use LAG() to get previous two numbers
SELECT DISTINCT num AS ConsecutiveNums 
FROM (SELECT id, num, LEAD(num, 1) OVER () AS n2, LEAD(num, 2) OVER () AS n3
    FROM Logs) t
WHERE num = n2  AND n2 = n3
```

##### Ex. (Leetcode 1709) Biggest Window Between Visits
```sql
SELECT user_id, MAX(daydiff) AS biggest_window
FROM
	(
	SELECT user_id, 
	   DATEDIFF(LEAD(visit_date, 1, '2021-01-01') OVER (PARTITION BY user_id ORDER BY visit_date), visit_date) AS daydiff
	FROM userVisits
	) a
GROUP BY 1
ORDER BY 1
```


* [ROW_NUMBER()](https://www.mysqltutorial.org/mysql-window-functions/mysql-row_number-function/): assigns a sequential number to each row in the result set


#### Aggregation
* COUNT(): return the number of rows that matches a specified criterion.
* SUM(): return the total sum of a numeric column
* AVG(): return the average of a numeric column

##### [Running total](https://popsql.com/learn-sql/mysql/how-to-calculate-cumulative-sum-running-total-in-mysql)
```sql
WITH ClientCountsByYear AS 
(SELECT YEAR(PurchaseDate) As PurchaseYear, COUNT(*) As ClientCounts
FROM Clients
GROUP BY 1)
SELECT PurchaseYear, SUM(ClientCounts) OVER (ORDER BY PurchaseYear) AS cum_sum
FROM ClientCountsByYear;
```

##### Ex. Given salary(department_id,employee_id,salary), list all employees with salary greater than the average department salary and also greather than $50K
```sql
SELECT employee_id
FROM 
(SELECT *, AVG(SALARY) OVER (PARTITION BY department_id) AS depart_avg
FROM salary) S
WHERE salary > 50000
```

#### [Combine strings under same group](https://stackoverflow.com/questions/31211506/how-stuff-and-for-xml-path-work-in-sql-server)
```sql
SELECT ID,  AllNames = STUFF(
  (SELECT ',' + name FROM temp1 t1 WHERE t1.id = t2.id
  FOR XML PATH ('')), 1, 1, '') 
FROM temp1 t2
GROUP BY ID;
```

### [Subqueries](https://mode.com/sql-tutorial/sql-sub-queries/)
* To aggregate in multiple stages
* In Conditional logic (in conjunction with WHERE, JOIN/ON, or CASE)
* Joining subqueries
* UNION to combine tables vertically


### CTE (Common Table Expressions)
A query that we create using WITH clause before writing the main query

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


### [Functions and variables](https://www.javatpoint.com/mysql-variables)
To store data in memory and can be used throughout the program
#### Variables

* User-Defined Variablestarts with @ symbol; pass values from one statement to another statement; does not reinitialized with NULL

```sql
# Assign the value in MySQL
SET @var_name = value;  
SELECT @var_name := value;  

# Assign the value in SQL Server
DECLARE @var_name AS INT = YEAR(GETDATE());
```
* Local Variable: strongly typed variable; is reinitialized with NULL value each time whenever stored procedure is called
* System Variable: various system variables that configure its operation, and each system variable contains a default value

#### UDF (User-Defined Functions)
Piece of code that extends the functionality of a SQL server that behaves just like a native (built-in) function

[Example of SQL on Databricks](https://databricks.com/blog/2021/10/20/introducing-sql-user-defined-functions.html)
```sql
CREATE FUNCTION blue()
  RETURNS STRING
  COMMENT 'Blue color code'
  LANGUAGE SQL
  RETURN '0000FF'
```

### Pratical Examples
#### [Find outliers](https://dataschool.com/how-to-teach-people-sql/how-to-find-outliers-with-sql/)
##### Order by
Sort the relevant values in both ascending and descending order
##### NTILES()
Separate our data into the same number of groups as the value inside the brackets

#### [Pivot](https://mode.com/sql-tutorial/sql-pivot-table/)
Rows to Columns; allow you to display row values as columns

MySQL does not have PIVOT function; use a CASE expression along with an aggregate function

[PIVOT and UNPIVOT in SQL Server](https://docs.microsoft.com/en-us/sql/t-sql/queries/from-using-pivot-and-unpivot?view=sql-server-ver15)

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

##### Ex. (Leetcode 618) Students Report By Geography if it is unknown which continent has the most students, 

```sql
## MAX ignores any null values. MAX returns NULL when there is no row to select.
SELECT
    MAX(CASE WHEN continent = 'America' THEN name END)AS America,
    MAX(CASE WHEN continent = 'Asia' THEN name END)AS Asia,
    MAX(CASE WHEN continent = 'Europe' THEN name END)AS Europe  
FROM (SELECT *, ROW_NUMBER() OVER (PARTITION BY continent ORDER BY name) AS id FROM student) AS t
GROUP BY id
```

##### Rank a table by revenue (Add a Rank Column), without using Rank() function
```sql
SELECT id, revenue, 
	(select count(*)+1 FROM tbl t2 
	WHERE t2.id = t1.id AND r1.revenue < r2.revenue)
FROM tbl t1
```

### Advanced topics 
#### Process JSON data 
##### [Flattening](https://www.holistics.io/blog/how-to-extract-nested-json-data-in-mysql-8-0/)
* Key-value object: a single record which consists of multiple named or indexed fields (or keys) paired with values
* Nested Array/Table: a table built with multiple key-value objects in a hierarchical format
##### Functions
* [JSON_EXTRACT()](https://dev.mysql.com/doc/refman/8.0/en/json-search-functions.html) OR ->>
* JSON_TABLE()

#### [Views](https://www.w3schools.com/sql/sql_view.asp)
* A _virtual_ table based on the result-set of an SQL statement
* Always shows up-to-date data when user queries it

```sql
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

#### [Stored Procedures](https://www.w3schools.com/sql/sql_stored_procedures.asp)
* A prepared SQL code that you can save, so the code can be reused over and over again
* Can also pass parameters to a stored procedure
```sql
CREATE PROCEDURE SelectAllClientss @State nvarchar(30)
AS
SELECT * FROM ClientTable WHERE State = @City
GO;
EXEC SelectAllCustomers @State = 'Illinois';

```
