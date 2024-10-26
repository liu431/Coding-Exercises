# Write your MySQL query statement below
select emp_name as manager_name , dep_id 
from Employees t
where position = 'Manager' 
    and dep_id in (select dep_id from (select dep_id, rank() over (order by count(emp_id) desc) as dep_rank
from Employees group by 1) a where dep_rank =  1)

order by dep_id
