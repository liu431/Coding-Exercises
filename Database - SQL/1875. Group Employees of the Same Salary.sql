# Write your MySQL query statement below
# Divide the employees into teams such that all the members on each team have the same salary
## Filter out the unique salary 
## use dense_rank to asisgn same rank to employees with same salary

SELECT *, DENSE_RANK() OVER (ORDER BY salary) AS team_id
FROM Employees
WHERE salary NOT IN 
(SELECT salary FROM Employees GROUP BY salary HAVING COUNT(*) = 1)
ORDER BY team_id, employee_id
