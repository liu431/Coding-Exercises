# Write your MySQL query statement below
# Find the employees who are high earners in each of the departments

## Use dense-rank() to rank employee's'salary for each department
WITH rankTBL AS (SELECT *, DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS SalaryRank
FROM Employee)

## Join Department to export result
SELECT D.name as Department, R.name AS Employee, salary as Salary
FROM rankTBL R
LEFT JOIN Department D ON D.id = R.departmentId
WHERE SalaryRank <= 3
