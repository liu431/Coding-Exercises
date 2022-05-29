# Write your MySQL query statement below
WITH tbl AS(
# 2019
(SELECT product_id, 2019 as report_year, 
CASE WHEN (YEAR(period_start) = 2019) and (YEAR(period_end) = 2019) THEN (DATEDIFF(period_end,period_start)+1) * average_daily_sales
WHEN YEAR(period_start) = 2019 and YEAR(period_end) = 2020 THEN (DATEDIFF('2019-12-31',period_start)+1) * average_daily_sales
WHEN YEAR(period_start) = 2018 and YEAR(period_end) = 2020 THEN (DATEDIFF('2019-12-31','2019-01-01')+1) * average_daily_sales
WHEN YEAR(period_start) = 2018 and YEAR(period_end) = 2019 THEN (DATEDIFF(period_end,'2019-01-01')+1) * average_daily_sales
ELSE NULL END AS total_amount
FROM SALES)

UNION

# 2018
(SELECT product_id, 2018 as report_year, 
CASE WHEN (YEAR(period_start) = 2018) and (YEAR(period_end) = 2018) THEN (DATEDIFF(period_end,period_start)+1) * average_daily_sales
WHEN YEAR(period_start) = 2018 and YEAR(period_end) = 2020 THEN (DATEDIFF('2018-12-31',period_start)+1) * average_daily_sales
WHEN YEAR(period_start) = 2018 and YEAR(period_end) = 2019 THEN (DATEDIFF('2018-12-31',period_start)+1) * average_daily_sales
ELSE NULL END AS total_amount
FROM SALES)

UNION

# 2020
(SELECT product_id, 2020 as report_year, 
CASE WHEN (YEAR(period_start) = 2020) and (YEAR(period_end) = 2020) THEN (DATEDIFF(period_end,period_start)+1) * average_daily_sales
WHEN (YEAR(period_start) = 2018 OR YEAR(period_start) = 2019) and YEAR(period_end) = 2020 THEN (DATEDIFF(period_end, '2020-01-01')+1) * average_daily_sales
ELSE NULL END AS total_amount
FROM SALES))

SELECT tbl.product_id, product_name, CONVERT(report_year, char) AS report_year, total_amount
FROM tbl 
LEFT JOIN Product on Product.product_id = tbl.product_id
WHERE total_amount IS NOT NULL
ORDER BY product_id, report_year
