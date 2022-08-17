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

## Get active drivers
col_activedrivers as 
(select mon, count(*) as ad from mon20
join Drivers D on mon20.mon >= date_format(D.join_date, "%Y-%m")
group by mon
order by mon),

## Get accepted_rides  
acc_rides as
(select *
from Rides
where ride_id in (select ride_id from AcceptedRides)),

col_acceptedrides as
(select mon, count(*) as ar from mon20
join acc_rides A on mon20.mon = date_format(A.requested_at, "%Y-%m")
group by mon
order by mon)

## join two metrics together
select 
    n as month, 
    coalesce(ad, 0) as active_drivers, 
    coalesce(ar, 0) as accepted_rides
from mon20
left join col_activedrivers using (mon)
left join col_acceptedrides using (mon)

