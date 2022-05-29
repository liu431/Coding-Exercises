# Write your MySQL query statement below
## Order purchase_date by user_id
## Use lag() to calculate date diff
## Return user ids with diff <= 7

select distinct user_id
from
(select user_id, datediff(lead(purchase_date, 1) over (partition by user_id order by purchase_date), purchase_date) as diff
from Purchases) t
where diff <= 7
