# Write your MySQL query statement below
# For each user, return the number of followers
SELECT user_id, COUNT(*) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id
