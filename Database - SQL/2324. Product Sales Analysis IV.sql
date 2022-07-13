# Write your MySQL query statement below
# need to left join Product table to calculate amount
# use group by to sum amounts for each user and product
# use rank to find the product id with highest amounts
# report only the rows with rank=1

with tbl_amt as 
    (select user_id, product_id, sum(quantity*price) as amt
    from Sales
    left join Product using(product_id)
    group by 1, 2)

select user_id, product_id
from
(select user_id, product_id, rank() over (partition by user_id order by amt desc) as amt_rank
from tbl_amt) t
where amt_rank=1

