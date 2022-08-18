# Write your MySQL query statement below
# Write your MySQL query statement below
## Get mon number recursively
WITH RECURSIVE month(n) AS (
    SELECT 1  
		UNION    
		SELECT n+1 FROM month    
    WHERE n < 12),

## Get year-mon as date format    
mon20 as 
(SELECT n, date_format(STR_TO_DATE(concat("2020", "-", n), "%Y-%m"),  "%Y-%m") AS mon 
FROM month),

## Get number of available drivers during a month
col_activedrivers as 
(select mon, count(*) as ad from mon20
join Drivers D on mon20.mon >= date_format(D.join_date, "%Y-%m")
group by mon
order by mon),

## Get number of working drivers
col_workingdrivers as
(select date_format(requested_at, "%Y-%m") as mon, count(distinct driver_id) as wd
from AcceptedRides
left join Rides using (ride_id)
where year(requested_at) = 2020
group by 1)

## join two metrics together
select 
    n as month, 
    round(coalesce(100 * wd / ad, 0), 2) as working_percentage 
from mon20
left join col_activedrivers using (mon)
left join col_workingdrivers using (mon)
