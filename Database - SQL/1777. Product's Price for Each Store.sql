# Write your MySQL query statement below

# Get price of products from each store
WITH 
s1 AS (SELECT product_id, price AS store1 FROM Products WHERE Store = 'store1'),
s2 AS (SELECT product_id, price AS store2 FROM Products WHERE Store = 'store2'),
s3 AS (SELECT product_id, price AS store3 FROM Products WHERE Store = 'store3')

# Join the price together
SELECT IDS.product_id, store1, store2, store3
FROM (SELECT DISTINCT product_id from Products) IDS
LEFT JOIN s1 ON IDS.product_id = s1.product_id
LEFT JOIN s2 ON IDS.product_id = s2.product_id
LEFT JOIN s3 ON IDS.product_id = s3.product_id

# 1795. Rearrange Products Table is the reverse arangement of the table
