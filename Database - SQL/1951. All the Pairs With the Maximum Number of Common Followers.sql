# Write your MySQL query statement below
# Find all the pairs of users with the maximum number of common followers
# Construct table with common follower numbers
# Find pairs with maxCommon
WITH Pairs AS (SELECT user1_id, user2_id, COUNT(*) AS CommF
            FROM (SELECT R1.user_id AS user1_id, R2.user_id AS user2_id
                FROM Relations R1
                JOIN Relations R2 USING (follower_id)
                WHERE R1.user_id < R2.user_id) t
            GROUP BY 1, 2)
            
SELECT user1_id, user2_id
FROM Pairs
WHERE CommF = (SELECT MAX(CommF) FROM Pairs)
