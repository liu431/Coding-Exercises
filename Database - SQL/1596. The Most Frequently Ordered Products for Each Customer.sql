# Write your MySQL query statement below
# Write an SQL query to find the most frequently ordered product(s) for each customer.
# Create a table with ranks of order counts sorted descendingly
WITH order_ranks AS 
(SELECT customer_id, product_id, RANK() OVER (PARTITION BY customer_id ORDER BY CTS DESC) AS RANKS
FROM (SELECT customer_id, product_id, COUNT(*) AS CTS FROM Orders GROUP BY customer_id, product_id) t)

# Return the result by getting the product name and limiting to those with most counts (rank = 1)
SELECT order_ranks.customer_id, order_ranks.product_id, product_name
FROM order_ranks
LEFT JOIN PRODUCTS ON PRODUCTS.product_id = order_ranks.product_id
WHERE RANKS = 1
