# Write your MySQL query statement below
# Find each query_name, the quality and poor_query_percentage
## quality: average of the ratio between query rating and its position
## poor query percentage: percentage of all queries with rating less than 3
SELECT query_name,
ROUND(AVG(rating/position), 2) AS quality, 
ROUND(100*SUM(rating < 3)/COUNT(*), 2) AS poor_query_percentage 
FROM Queries
GROUP BY query_name
