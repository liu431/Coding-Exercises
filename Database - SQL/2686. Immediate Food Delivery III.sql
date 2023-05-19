# Write your MySQL query statement below
select
    order_date,
    round(100.0 * sum(case when order_date = customer_pref_delivery_date then 1 else 0 end) / count(delivery_id), 2) as immediate_percentage
from Delivery
group by 1
order by 1
