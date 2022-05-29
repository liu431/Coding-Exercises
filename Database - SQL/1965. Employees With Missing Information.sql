# Write your MySQL query statement below
# Report the IDs of all the employees with missing information
## The employee's salary is missing
SELECT employee_id 
FROM Employees
WHERE employee_id NOT IN (SELECT employee_id FROM Salaries)
UNION
## The employee's name is missing
SELECT employee_id 
FROM Salaries
WHERE employee_id NOT IN (SELECT employee_id FROM Employees)
ORDER BY employee_id
