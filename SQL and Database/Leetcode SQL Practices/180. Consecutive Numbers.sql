# Write your MySQL query statement below
# Find all numbers that appear at least three times consecutively
# Use LAG() to get previous two numbers
SELECT DISTINCT num AS ConsecutiveNums 
FROM (SELECT id, num, LEAD(num, 1) OVER () AS n2, LEAD(num, 2) OVER () AS n3
    FROM Logs) t
WHERE num = n2  AND n2 = n3

