# Write your MySQL query statement below
select user_id, sum(quantity*P.price) as spending
from Sales S
left join Product P using (product_id)
group by 1
order by 2 desc, 1 asc
