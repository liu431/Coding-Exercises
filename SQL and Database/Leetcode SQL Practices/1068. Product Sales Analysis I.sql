# Write your MySQL query statement below
# Report the product_name, year, and price for each sale_id in the Sales table.
SELECT product_name, year, price
FROM Sales
JOIN Product ON Product.product_id = Sales.product_id
