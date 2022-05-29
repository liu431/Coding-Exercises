# Write your MySQL query statement below
# Report the number of users that used each bus.
## Number of users for t_bus are the t_passenger between previous and current t_bus
WITH B AS (SELECT *, COALESCE(LAG(arrival_time) OVER (ORDER BY arrival_time), 0) AS prev_leave_time
FROM Buses),

cnt AS (SELECT bus_id, COUNT(*) AS passengers_cnt 
FROM Passengers P
LEFT JOIN B ON P.arrival_time > B.prev_leave_time AND P.arrival_time <= B.arrival_time 
GROUP BY bus_id)

SELECT Buses.bus_id, COALESCE(passengers_cnt, 0) AS passengers_cnt
FROM Buses
LEFT JOIN cnt USING (bus_id)
ORDER BY bus_id
