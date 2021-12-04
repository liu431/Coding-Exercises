## SQL Notes

#### Rank()
* dense_rank(): assign rank to each row within a partition without gaps
* rank(): assign rank to each row within a partition with gaps
* percent_rank():returns the percentile rank of a row within a partition that ranges from 0 to 1

```sql
SELECT product_id, year, RANK() OVER (PARTITION BY product_id ORDER BY year) AS 'rank' 
FROM Sales;
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
