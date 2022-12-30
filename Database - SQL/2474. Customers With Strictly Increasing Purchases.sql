# Write your MySQL query statement below
## 1. aggregate orders by customer and year
## 2. assign rank to total purchases amount
## 3. assign rank to year
## 4. rank the customer with two ranks equal

with agg as (
    select customer_id, year(order_date) as years, sum(price) as total
    from Orders
    group by 1, 2),

agg_with_rank as (
    select 
        customer_id, 
        rank() over (partition by customer_id order by years) != rank() over (partition by customer_id order by total) as rank_diff,
        years, 
        total
    from agg),

cutsomer_with_gap as (
    select customer_id, (max(years) - min(years) + 1) != count(*) as with_gap
    from agg
    group by 1
)

select distinct customer_id
from agg
where customer_id not in (select customer_id from agg_with_rank where rank_diff = 1)
and customer_id not in (select customer_id from cutsomer_with_gap where with_gap = 1)
