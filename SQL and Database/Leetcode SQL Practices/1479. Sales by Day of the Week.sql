# Write your MySQL query statement below
# Report how many units in each category have been ordered on each day of the week
SELECT i.item_category AS Category,
SUM(CASE WHEN DayOfWeek(o.order_date)=2 THEN quantity ELSE 0 END) AS MONDAY,
SUM(CASE WHEN DayOfWeek(o.order_date)=3 THEN quantity ELSE 0 END) AS TUESDAY,
SUM(CASE WHEN DayOfWeek(o.order_date)=4 THEN quantity ELSE 0 END) AS WEDNESDAY,
SUM(CASE WHEN DayOfWeek(o.order_date)=5 THEN quantity ELSE 0 END) AS THURSDAY,
SUM(CASE WHEN DayOfWeek(o.order_date)=6 THEN quantity ELSE 0 END) AS FRIDAY,
SUM(CASE WHEN DayOfWeek(o.order_date)=7 THEN quantity ELSE 0 END) AS SATURDAY,
SUM(CASE WHEN DayOfWeek(o.order_date)=1 THEN quantity ELSE 0 END) AS SUNDAY
FROM items i
LEFT JOIN Orders o ON o.item_id = i.item_id
GROUP BY i.item_category
ORDER BY i.item_category
