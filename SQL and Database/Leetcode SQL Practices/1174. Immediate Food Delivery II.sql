# Write your MySQL query statement below

## Filter Deliverys to keep first orders only
## Use CASE to flag the immediate orders
## Calculate the percentage of immediate orders in the first orders of all customers
## Note: customer_pref_delivery_date is random after grouping by the customer_id, and not guarantee to align with the minimum order_date row.

SELECT ROUND(100 * AVG(order_date=customer_pref_delivery_date), 2) AS immediate_percentage 
FROM Delivery
WHERE (customer_id, order_date) IN
(SELECT customer_id, MIN(order_date)
FROM Delivery
GROUP BY 1)



