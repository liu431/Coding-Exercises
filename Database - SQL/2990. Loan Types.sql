# Write your MySQL query statement below
select user_id 
from 
(
select 
    user_id,
    sum(loan_type = 'Mortgage') as cts_mortage,
    sum(loan_type = 'Refinance') as cts_ref
from Loans
group by 1
) as t
where cts_mortage > 0 and cts_ref > 0
order by 1 
