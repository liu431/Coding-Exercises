# Write your MySQL query statement below
# Report the second-degree users and the number of their followers.
## A second-degree follower is a user who: follows at least one user, and is followed by at least one user.
## Create followers and followees count table
## Filter the table to report second-degree users

WITH follower_cts_tbl AS (SELECT followee AS ID, COUNT(*) AS follower_cts 
From Follow
GROUP BY 1),
followee_cts_tbl AS (SELECT follower AS id, COUNT(*) AS followee_cts 
From Follow
GROUP BY 1)

SELECT follower_cts_tbl.ID AS follower, follower_cts AS num
FROM follower_cts_tbl
JOIN followee_cts_tbl USING (ID)
ORDER BY follower

