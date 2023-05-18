# Write your MySQL query statement below
with tbl_ranked as (
    select 
        *, 
        rank() over (partition by emp_id order by salary desc) as salary_rank
    from Salary)

select emp_id, firstname, lastname, salary, department_id
from tbl_ranked
where salary_rank = 1
