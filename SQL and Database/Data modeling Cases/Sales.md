- Sales (date, salesid, marketid, region, salesamount)

a. Total sales of each region in the past one month
```sql
SELECT region, SUM(salesamount) AS totalsales
FROM Sales
WHERE DATEDIFF(NOW(), date) <= 30
```

b. List of marketids that have above-average salesamount in each region
```sql
WITH avgsales_tbl AS (SELECT region, AVG(salesamount) AS avgsales
FROM Sales
GROUP BY 1)
SELECT DISTINCT Sales.region, Sales.marketid
FROM Sales
LEFT JOIN avgsales_tbl USING (REGION)
WHERE salesamount > avgsales
```
