# Write your MySQL query statement below

with task_day as 
(select 
    case when dayofweek(submit_date) in (1, 7) then 1 else 0 end as wday
from Tasks)

select sum(wday=1) as weekend_cnt, sum(wday=0) as working_cnt from task_day
