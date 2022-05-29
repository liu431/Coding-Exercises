# Write your MySQL query statement below
# Report the ids and the names of all managers, the number of employees who report directly to them
SELECT employee_id, name, reports_count, average_age
FROM Employees
JOIN 
(SELECT reports_to, COUNT(*) AS reports_count, ROUND(AVG(age)) AS average_age
FROM Employees WHERE reports_to IS NOT NULL GROUP BY reports_to) M
ON M.reports_to = Employees.employee_id
ORDER BY employee_id
