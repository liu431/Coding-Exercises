# Write your MySQL query statement below
## Get a pivot table with product_id, purchase_year with counts>3
## use lag() to keep the consecutive years

with t as
(select product_id, year(purchase_date) as purchase_year
from Orders 
group by 1, 2
having count(*) >= 3
order by 1, 2),

t2 as
(select product_id, purchase_year, purchase_year - lag(purchase_year) over (partition by product_id) as year_diff
from t)

select distinct product_id
from t2
where year_diff = 1
