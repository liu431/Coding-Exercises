# Write your MySQL query statement below
# Calculate the cumulative salary summary for every employee in a single unified table

## Subquery: Except the most recent month of each employee
WITH Emp AS (SELECT *
FROM
(SELECT *, RANK() OVER (PARTITION BY id ORDER BY month DESC) AS mon_rank
FROM Employee) t
WHERE mon_rank != 1)

## Use self join if you have only one table but to write a complex query
SELECT E1.id, E1.month, (E1.salary + IFNULL(E2.salary,0) + IFNULL(E3.salary,0)) AS salary
FROM Emp E1
LEFT JOIN Emp E2 ON E1.id = E2.id AND E1.month = E2.month + 1
LEFT JOIN Emp E3 ON E2.id = E3.id AND E2.month = E3.month + 1 AND E1.month = E3.month + 2
