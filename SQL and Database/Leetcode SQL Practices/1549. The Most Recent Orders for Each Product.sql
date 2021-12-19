# Write your MySQL query statement below
# Find the most recent order(s) of each product

## Subquery 1: Assign rank to the order date by product
WITH order_rank AS (
SELECT product_name, product_id, order_id, order_date,
RANK() OVER (PARTITION BY product_id ORDER BY order_date DESC) AS timerank
FROM Products
JOIN Orders USING (product_id))

## Filter results to get the most recent orders by product
SELECT product_name, product_id, order_id, order_date
FROM order_rank
WHERE timerank = 1
ORDER BY product_name, product_id, order_id 
