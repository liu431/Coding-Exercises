# Write your MySQL query statement below
# CTE: products that have changed prices
## Use rank() function to get the latest price
with Changes as (select product_id, new_price, rank () over (partition by product_id order by change_date desc) as ranks
from Products
where change_date <= '2019-08-16')

# Main Output
## Assume the price of all products before any change is 10
select distinct P.product_id, ifnull(C.new_price, 10) as price 
from Products P
left join Changes C on C.product_id=P.product_id
where ifnull(ranks, 1) = 1
