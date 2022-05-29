# Write your MySQL query statement below
# Find all the strong friendships; strong if x and y have at least three common friends
## Self join 1: find user1's friends
## Self join 2: find user2's friends
## Find pairs that appear twice
## Group by to get counts

WITH AllPairs AS (SELECT user1_id, user2_id
                    FROM Friendship
                    UNION
                    SELECT user2_id user1_id, user1_id user2_id
                    FROM Friendship)
                    
SELECT F.user1_id, F.user2_id, COUNT(A2.user2_id) AS common_friend
FROM Friendship F
JOIN AllPairs A1 ON F.user1_id = A1.user1_id
JOIN AllPairs A2 ON F.user2_id = A2.user1_id AND A1.user2_id = A2.user2_id
GROUP BY 1, 2
HAVING common_friend >= 3
 
