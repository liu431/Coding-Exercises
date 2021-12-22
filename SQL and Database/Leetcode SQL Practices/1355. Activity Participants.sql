# Write your MySQL query statement below
# Find the names of all the activities with neither the maximum nor the minimum number of participants

## Subquery: activity counts
WITH cts AS (SELECT activity, COUNT(*) AS activity_cts
FROM Friends
GROUP BY activity)

## Use WHERE to exclude activities with the maximum and the minimum number of participants
SELECT activity
FROM cts
WHERE activity_cts != (SELECT MAX(activity_cts) FROM cts) AND activity_cts != (SELECT MIN(activity_cts) FROM cts)
