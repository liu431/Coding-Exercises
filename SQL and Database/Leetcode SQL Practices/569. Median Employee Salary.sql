# Write your MySQL query statement below
# Find the median salary of each company
## Use RANK() to get index by group
## Medians are ones with id between (n/2) and (n/2) + 1

SELECT id, company, salary
FROM (SELECT *, 
        ROW_NUMBER() OVER(PARTITION BY company ORDER BY salary) AS ind, 
        COUNT(*) OVER (PARTITION BY company) AS N 
        FROM Employee) t
WHERE ind BETWEEN N/2 AND (N/2 + 1)
