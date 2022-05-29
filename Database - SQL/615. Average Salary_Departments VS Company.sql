# Write your MySQL query statement below
# Report the comparison result (higher/lower/same) of the average salary of employees in a department to the company's average salary

## Table for getting the company's average salary by month
WITH compAvgTbl AS 
(SELECT LEFT(pay_date, 7) as pay_month, ROUND(AVG(amount), 2) AS comAvg
FROM Salary 
GROUP BY pay_month)

## Result table
SELECT LEFT(S.pay_date, 7) as pay_month, department_id, 
## Compare department and company averages
CASE WHEN ROUND(AVG(amount), 2) > comAvg THEN 'higher'
WHEN ROUND(AVG(amount), 2) < comAvg THEN 'lower'
ELSE 'same' END AS comparison
FROM Salary S
LEFT JOIN Employee E ON E.employee_id = S.employee_id
LEFT JOIN compAvgTbl C on C.pay_month = LEFT(S.pay_date, 7)
GROUP BY pay_month, department_id
