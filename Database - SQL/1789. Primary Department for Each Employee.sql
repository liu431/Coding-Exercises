# Write your MySQL query statement below
# Report all the employees with their primary department. For employees who belong to one department, report their only department.

## For employees with one department, use associated flag
SELECT employee_id, department_id 
FROM Employee
GROUP BY employee_id
HAVING COUNT(*) = 1
UNION
## For employees with multiple department, use WHERE to find flag with 'Y'
SELECT employee_id, department_id 
FROM Employee
WHERE primary_flag = 'Y'
