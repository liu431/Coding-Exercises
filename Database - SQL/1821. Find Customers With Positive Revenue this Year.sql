# Write your MySQL query statement below
# Report the customers with postive revenue in the year 2021
SELECT customer_id
FROM Customers
WHERE year = 2021 AND revenue > 0
