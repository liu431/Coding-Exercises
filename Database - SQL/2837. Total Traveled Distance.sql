# Write your MySQL query statement below
select 
    user_id,
    name,
    coalesce(sum(distance), 0) as 'traveled distance'
from Users
left join Rides using (user_id)
group by 1
order by 1
