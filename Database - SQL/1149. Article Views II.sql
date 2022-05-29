# Write your MySQL query statement below
# Find all the people who viewed more than one article on the same date
## Group by viewer_id and date to get counts of distinct article_id
## Filter the results so that count is more than 1
SELECT DISTINCT viewer_id AS id
FROM Views
GROUP BY viewer_id, view_date
HAVING COUNT(DISTINCT article_id) > 1
ORDER BY id
