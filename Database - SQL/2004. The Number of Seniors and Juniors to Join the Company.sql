# Write your MySQL query statement below
# Find the number of seniors and juniors hired with budget $70000
# 1. Hiring the largest number of seniors.
# 2. After hiring the maximum number of seniors, use the remaining budget to hire the largest number of juniors.

## First, use running total to find the number of Seniors and cost
## Second, use running total to find juniors to hire with remaining budget

WITH SeniorR AS 
    (SELECT COUNT(employee_id) AS SeniorHires, COALESCE(MAX(SeniorCost),0) AS SeniorCost
    FROM (SELECT employee_id, SUM(salary) OVER (ORDER BY salary) AS SeniorCost
        FROM Candidates
        WHERE experience = 'Senior') S
    WHERE SeniorCost <= 70000),
JuniorR AS 
    (SELECT COUNT(employee_id) AS JuniorHires
    FROM (SELECT employee_id, SUM(salary) OVER (ORDER BY salary) AS JuniorCost
        FROM Candidates
        WHERE experience = 'Junior') J
    WHERE JuniorCost <= 70000 - (SELECT SeniorCost FROM SeniorR))
    
SELECT 'Senior' AS experience, SeniorHires AS accepted_candidates
FROM SeniorR
UNION
SELECT 'Junior' AS experience, JuniorHires AS accepted_candidates
FROM JuniorR
