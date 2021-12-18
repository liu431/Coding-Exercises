# Write your MySQL query statement below

# Confirmation rate of a user is the number of 'confirmed' messages divided by the total number of requested confirmation messages
WITH tbl AS (SELECT user_id, 
SUM(action = "confirmed")/COUNT(*)  AS confirmation_rate
FROM Confirmations
GROUP BY user_id)

# Use left join hee to keep the ids that only exist in Signups table
SELECT Signups.user_id, ROUND(IFNULL(confirmation_rate, 0), 2) AS confirmation_rate
FROM Signups 
LEFT JOIN tbl ON tbl.user_id = Signups.user_id

