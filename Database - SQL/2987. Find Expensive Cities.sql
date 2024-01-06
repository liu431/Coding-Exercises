# Write your MySQL query statement below
# look at the average of each city and then compare with national mean
with city_avg as (
    select 
        city,
        avg(price) as avg_price
    from Listings
    group by 1
)
select city
from city_avg
where avg_price > (select avg(price) from Listings)
order by 1
