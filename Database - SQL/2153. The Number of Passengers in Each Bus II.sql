/* Write your T-SQL query statement below */
--Reference: https://leetcode.com/problems/the-number-of-passengers-in-each-bus-ii/solutions/1727603/mssql-lag-and-recursive-cte/?orderBy=most_votes

with c1 as -- Find the previous bus arrival time 
(
    select
		rn = row_number() over (order by  arrival_time),  -- create a row number for the sequence of the bus.
		bus_id,
		arrival_time,
		prev_time = lag(arrival_time, 1 , -999) over(order by arrival_time), 
		capacity
    from Buses
),

c2 as -- Find how many people current bus needs to take, without thinking of the remaining passengers from the previous buses
(
	select 
		c1.rn,
		c1.bus_id,
		c1.capacity,
		curr_passenger_cnt = count(p.passenger_id)
	from c1 left outer join Passengers p on p.arrival_time <= c1.arrival_time and p.arrival_time > c1.prev_time
	group by c1.rn, c1.bus_id, c1.capacity
)
, r_cte as  
    -- find how many people previous bus left, and how many current bus can take.
    -- current bus pick = prev_remaining + current_Passenger
    -- current bus remaining = max(0, prev_remaining + current_Passenger - capacity)
(
	select 
		rn,
		bus_id,
		capacity,
		curr_passenger_cnt,
		accumulated_remaining = case when curr_passenger_cnt - capacity <= 0 then 0 else curr_passenger_cnt - capacity end  
	from c2 where rn = 1 --starting from the first arrival bus

	union all 
		
	select    
		c2.rn, 
		c2.bus_id,
		c2.capacity,
		curr_passenger_cnt = c2.curr_passenger_cnt + c.accumulated_remaining,
		accumulated_remaining = case when c2.curr_passenger_cnt + c.accumulated_remaining - c2.capacity <= 0 then 0 else c2.curr_passenger_cnt + c.accumulated_remaining - c2.capacity end
	from r_cte c inner join c2 on c2.rn = c.rn + 1
)
select 
    bus_id,
    passengers_cnt = case when accumulated_remaining > 0 then capacity else curr_passenger_cnt end  
from r_cte
order by bus_id
