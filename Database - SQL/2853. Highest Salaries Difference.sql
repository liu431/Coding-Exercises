# Write your MySQL query statement below

with mkt_s as (select 1 as id, max(salary) as m_s from Salaries where department = 'Marketing'),
eng_s as (select 1 as id, max(salary) as e_s from Salaries where department = 'Engineering')
select abs(m_s - e_s) as salary_difference 
from mkt_s
join eng_s using (id)
