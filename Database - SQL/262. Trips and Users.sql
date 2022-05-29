# Write your MySQL query statement below
# Find cancellation rate of requests with unbanned users
SELECT request_at AS Day,
# Calculate cancellation rate with aggregation function
ROUND(SUM(CASE WHEN status = "completed" THEN 0 ELSE 1 END)/COUNT(*), 2) AS 'Cancellation Rate'
FROM Trips
# Apply criterias
WHERE request_at BETWEEN "2013-10-01" AND "2013-10-03"
# Exclude banned users
AND client_id NOT IN (SELECT users_id FROM Users WHERE banned='Yes')
AND driver_id NOT IN (SELECT users_id FROM Users WHERE banned='Yes')
GROUP BY 1
