# Write your MySQL query statement below
## Create table to get the rank of the year of every product sold
WITH TBL AS (SELECT sale_id, product_id, year, quantity, price, RANK() OVER (PARTITION BY product_id ORDER BY year) AS yearrank
FROM Sales)
# Filter results with the first year sales of every product
SELECT product_id, year AS first_year, quantity, price
FROM TBL 
WHERE yearrank = 1
