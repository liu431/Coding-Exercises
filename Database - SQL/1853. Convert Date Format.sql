# Write your MySQL query statement below
# Convert each date in Days into a string formatted as "day_name, month_name day, year"
SELECT DATE_FORMAT(day, "%W, %M %e, %Y") AS day
FROM Days
