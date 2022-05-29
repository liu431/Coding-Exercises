# Write your MySQL query statement below
# CTE: group product names by customer
WITH AGG AS (SELECT customer_id, GROUP_CONCAT(product_name) AS allproducts
FROM Orders
GROUP BY customer_id)

# Report the customer_id and customer_name of customers who bought products "A", "B" but did not buy the product "C" 
SELECT AGG.customer_id, customer_name
FROM AGG 
JOIN Customers ON Customers.customer_id = AGG.Customer_id
WHERE allproducts LIKE '%A%'  AND allproducts LIKE '%B%' AND allproducts NOT LIKE '%C%' 
