# Write your MySQL query statement below
# product_name in lowercase without leading or trailing white spaces.
# sale_date in the format ('YYYY-MM').
# total the number of times the product was sold in this month.

SELECT LOWER(TRIM(product_name)) AS product_name, DATE_FORMAT(sale_date, '%Y-%m') AS sale_date, COUNT(*) AS total
FROM Sales
GROUP BY 1, 2
ORDER BY 1, 2
