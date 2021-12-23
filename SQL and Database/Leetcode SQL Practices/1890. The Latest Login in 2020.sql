# Write your MySQL query statement below
# Report the latest login for all users in the year 2020
## Use MAX() is more efficient than RANK() as we only need the latest login
SELECT user_id, MAX(time_stamp) as last_stamp
FROM Logins 
WHERE YEAR(time_stamp) = 2020
GROUP BY user_id
