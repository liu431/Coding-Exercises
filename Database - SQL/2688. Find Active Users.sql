# Write your MySQL query statement below
with diff_tbl as (
select 
    user_id,
    created_at,
    lag(created_at) over (partition by user_id order by created_at) as prev_day
from Users)

select 
    distinct user_id
from diff_tbl
where datediff(created_at, prev_day) <= 7
