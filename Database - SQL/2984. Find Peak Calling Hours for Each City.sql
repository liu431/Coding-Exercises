# Write your MySQL query statement below
with tbl_cts as (
    select
        city,
        hour(call_time) as peak_calling_hour,
        count(hour(call_time)) as number_of_calls 
    from Calls
    group by 1, 2
),
tbl_rk as (
    select 
        city,
        peak_calling_hour,
        number_of_calls,
        rank() over (partition by city order by number_of_calls desc) as hour_rank
    from tbl_cts
)
select 
    city,
    peak_calling_hour,
    number_of_calls 
from tbl_rk
where hour_rank = 1
order by peak_calling_hour desc, city desc
