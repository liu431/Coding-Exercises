# Write your MySQL query statement below
# Find the average number of sessions per user for a period of 30 days ending 2019-07-27
## The sessions we want to count for a user are those with at least one activity in that time period.

SELECT IFNULL(ROUND(COUNT(DISTINCT session_id)/COUNT(DISTINCT user_id), 2) , 0.00) AS average_sessions_per_user 
FROM Activity
WHERE DATEDIFF('2019-07-27', activity_date) < 30


