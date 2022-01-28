# Write your MySQL query statement below
# Write an SQL query to report the similar friends of Leetcodify users. A user x and user y are similar friends if: 1. Users x and y are friends, and 2. Users x and y listened to the same three or more different songs on the same day.

## From Listens, get all (x, y) that satisfies condition 2
## Match with Friendship to satisfy condition 1

WITH cond2 AS (SELECT L1.day, L1.user_id AS user1_id, L2.user_id AS user2_id
    FROM Listens L1, Listens L2
    WHERE L1.user_id < L2.user_id and L1.song_id = L2.song_id and L1.day = L2.day
    GROUP BY L1.day, L1.user_id, L2.user_id
    HAVING COUNT(DISTINCT L1.song_id) >= 3)
    
SELECT DISTINCT F.user1_id, F.user2_id
FROM Friendship F
JOIN cond2 USING (user1_id, user2_id) 
ORDER BY 1
