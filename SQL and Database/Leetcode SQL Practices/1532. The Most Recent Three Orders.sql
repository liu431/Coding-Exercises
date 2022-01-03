# Write your MySQL query statement below
# Find the most recent three orders of each user. If a user ordered less than three orders, return all of their orders
## Subquery: assign rank to each customer's order dates in descedning order

SELECT name AS customer_name, Customers.customer_id, order_id, order_date
FROM 
    (SELECT *, RANK() OVER (PARTITION BY customer_id ORDER BY order_date DESC) AS order_rank
    FROM Orders) t
LEFT JOIN Customers USING (customer_id)
WHERE order_rank <= 3
ORDER BY 1, 2, 4 desc
