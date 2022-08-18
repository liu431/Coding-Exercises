# Write your MySQL query statement below
## 1: get ride_distance and ride_duration by month
## 2. use lag() and lead() to get the previous and after months' values
WITH RECURSIVE month(n) AS (
    SELECT 1  
		UNION    
		SELECT n+1 FROM month    
    WHERE n < 12),

## Get year-mon as date format    
mon20 as 
(SELECT n, date_format(STR_TO_DATE(concat("2020", "-", n), "%Y-%m"),  "%Y-%m") AS mon 
FROM month), 

## summed values by month
sum_val as 
(select 
    month(requested_at) as n,
    sum(ride_distance) as sum_dist,
    sum(ride_duration) as sum_dur
from AcceptedRides 
left join Rides using (ride_id)
where year(requested_at) = 2020
group by 1),

## summed values by all months
sum_val_allmonth as 
(select 
    n, 
    coalesce(sum_dist, 0) as sum_dist,
    coalesce(sum_dur, 0) as sum_dur
from mon20
left join sum_val using (n)),

## calculate the every 3-month window  
val_all as
(select n as month, 
    round((sum_dist + lead(sum_dist) over () + lead(sum_dist, 2) over ()) / 3, 2) as average_ride_distance,
    round((sum_dur + lead(sum_dur) over () + lead(sum_dur, 2) over ()) / 3, 2) as average_ride_duration
from sum_val_allmonth)

## remove Nov and Dec
select *
from val_all
where month <= 10
