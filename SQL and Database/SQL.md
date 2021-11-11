## SQL Notes

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

