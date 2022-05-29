# Write your MySQL query statement below
# Rearrange the Products table so that each row has (product_id, store, price)
# Use UNION to combine product_id and prices from 3 stores
# Use WHERE price IS NOT NULL to exclude products that are not available in that store 
SELECT product_id, 'store1' as store, store1 as price FROM Products WHERE store1 IS NOT NULL
UNION
SELECT product_id, 'store2' as store, store2 as price FROM Products WHERE store2 IS NOT NULL
UNION
SELECT product_id, 'store3' as store, store3 as price FROM Products WHERE store3 IS NOT NULL
