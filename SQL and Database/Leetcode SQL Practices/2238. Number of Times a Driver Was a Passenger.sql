# Write your MySQL query statement below
## First, find the cts for passengers who are also drivers
## Second, find the unique driver id list
### Third, make teh table
with pass_cts as (select passenger_id as driver_id, count(ride_id) as cts
from Rides
where passenger_id in (select driver_id from Rides)
group by 1),

driver_ids as 
(select distinct driver_id from Rides)

select driver_id, ifnull(cts, 0) as cnt
from driver_ids 
left join pass_cts using (driver_id)
