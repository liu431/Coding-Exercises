# Write your MySQL query statement below
# Use left(column, digits) to exclude the dates
# Use case when to filter the approved counts and amounts
select left(trans_date, 7) as month, country, count(trans_date) as trans_count, count(case when state='approved' then 1 end) as approved_count, sum(amount) as trans_total_amount, sum(case when state='approved' then amount else 0 end) as approved_total_amount
from Transactions
group by left(trans_date, 7), country
