# Write your MySQL query statement below
# Report for every date within at most 90 days from today, the number of users that logged in for the first time on that date
SELECT login_date, COUNT(*) AS user_count
FROM (
    # Table with users who first logged in at most 90 days from today
    SELECT user_id, MIN(activity_date) AS login_date  
    FROM Traffic
    WHERE activity = 'login'
    GROUP BY 1
    HAVING DATEDIFF('2019-06-30', login_date) <= 90) t
    
GROUP BY 1
