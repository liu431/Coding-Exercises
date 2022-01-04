# Write your MySQL query statement below
# Write an SQL query to report all the orders based on the following criteria: If a customer has at least one order of type 0, do not report any order of type 1 from that customer. Otherwise, report all the orders of the customer.

## Use NOT IN to filter out this type of customer ids
WITH C AS (SELECT customer_id
            FROM Orders
            GROUP BY customer_id
            HAVING SUM(order_type=0) > 0)
SELECT * 
FROM Orders
WHERE customer_id NOT IN (SELECT customer_id FROM C)
UNION ALL
SELECT * 
FROM Orders
WHERE customer_id IN (SELECT customer_id FROM C) AND order_type != 1
