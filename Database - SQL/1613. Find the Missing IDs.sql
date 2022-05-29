# Write your MySQL query statement below
# Find the missing customer IDs

# Get id range from 1 to max customer_id by recursive function
WITH recursive id_range AS 
    (
        SELECT 1 AS ids
        UNION ALL
        SELECT ids + 1
        FROM id_range
        WHERE ids < (SELECT MAX(customer_id) FROM Customers)
    )

# Exclude ids that are in the Customers table
SELECT ids
FROM id_range
WHERE ids NOT IN (SELECT customer_id FROM Customers)
