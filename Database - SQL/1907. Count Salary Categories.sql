# Write your MySQL query statement below

# Subquery 1: catgegory counts from Accounts
WITH inc_category AS 
(SELECT category, COUNT(*) AS accounts_count FROM
(SELECT 
CASE WHEN income > 50000 THEN 'High Salary'
WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary'
ELSE 'Low Salary' END AS category
FROM Accounts) t
GROUP BY category),

# Subquery 2: category list
# Need this as he result table must contain all three categories.
bins AS (
SELECT 'High Salary' AS category
UNION 
SELECT 'Average Salary'
UNION
SELECT 'Low Salary')

# Report the number of bank accounts of each salary category
SELECT bins.category, IFNULL(accounts_count, 0) AS accounts_count
FROM bins
LEFT JOIN inc_category USING (category)
