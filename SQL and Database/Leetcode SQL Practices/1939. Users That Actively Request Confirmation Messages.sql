# Write your MySQL query statement below
# Find the IDs of the users that requested a confirmation message twice within a 24-hour window.
SELECT DISTINCT user_id
FROM
(SELECT *, ((TIMESTAMPDIFF(SECOND, LAG(time_stamp) OVER (PARTITION BY user_id ORDER BY time_stamp), time_stamp)) / 3600) AS diff
FROM Confirmations) t
WHERE diff <= 24
