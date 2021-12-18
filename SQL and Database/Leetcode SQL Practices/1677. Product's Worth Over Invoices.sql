# Write your MySQL query statement below
# For all products, return each product name with the total amount due, paid, canceled, and refunded across all invoices
SELECT name, 
IFNULL(SUM(rest), 0) AS rest, IFNULL(SUM(paid), 0) AS paid, 
IFNULL(SUM(canceled), 0) AS canceled, IFNULL(SUM(refunded), 0) AS refunded
FROM Product
LEFT JOIN Invoice USING(product_id)
GROUP BY name
ORDER BY name
