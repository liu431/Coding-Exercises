# Write your MySQL query statement below
# Report the ID of the airport with the most traffic
## Traffic: number of flights that either departed from or arrived at the airport
WITH CTS AS (SELECT id, RANK() OVER(ORDER BY SUM(flights_count) DESC) AS cts_rank
FROM (SELECT departure_airport AS id, flights_count
FROM Flights
UNION ALL
SELECT arrival_airport AS id, flights_count
FROM Flights) t
GROUP BY id)

SELECT id AS airport_id
FROM CTS
WHERE cts_rank = 1
