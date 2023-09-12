# Write your MySQL query statement below
select
    flight_id,
    case when capacity > count(passenger_id) then count(passenger_id) else capacity end as booked_cnt,
    case when capacity > count(passenger_id) then 0 else count(passenger_id) - capacity end as waitlist_cnt
from Flights
left join Passengers using (flight_id)
group by 1
order by 1
