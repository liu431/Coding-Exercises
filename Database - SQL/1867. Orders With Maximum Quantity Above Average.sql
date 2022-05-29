# Write your MySQL query statement below
# Find the order_id of all imbalanced orders
## An imbalanced order is one whose maximum quantity is strictly greater than the average quantity of every order (including itself)

SELECT DISTINCT order_id
FROM OrdersDetails 
GROUP BY order_id
HAVING MAX(quantity) > ALL(SELECT AVG(quantity) FROM OrdersDetails GROUP BY order_id)
