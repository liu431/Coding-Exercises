# Write your MySQL query statement below
# the number of customers who had at least one bill with an amount strictly greater than 500
SELECT COUNT(DISTINCT customer_id) AS rich_count
FROM STORE
WHERE amount > 500
