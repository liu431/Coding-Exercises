# Write your MySQL query statement below
WITH 
# Get excellent student counts from NYU
NYCts AS (SELECT COUNT(*) AS NY FROM NewYork WHERE score >= 90),
# Get excellent student counts from CU
CACts AS (SELECT COUNT(*) AS CA FROM California WHERE score >= 90)
# Compare
SELECT CASE 
WHEN NY > CA THEN "New York University"
WHEN NY < CA THEN "California University"
ELSE "No Winner"  END AS winner
FROM NYCts, CACts
