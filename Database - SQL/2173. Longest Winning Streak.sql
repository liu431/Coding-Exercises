# Write your MySQL query statement below
# Encode the result to 1,2,3 and then do rank()
WITH cte AS
(SELECT *,
    ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY match_day) ck1,
    ROW_NUMBER() OVER (PARTITION BY player_id, result ORDER BY match_day) ck2
FROM Matches),

all_player as (
    select distinct player_id from Matches
),

steaks as (
    SELECT player_id, 
    COUNT(match_day) streak
    FROM cte
    WHERE result = 'Win'
    GROUP BY 1, ck1-ck2
)

SELECT m.player_id, IFNULL(MAX(streak), 0) longest_streak
FROM all_player m 
LEFT JOIN steaks t using (player_id)
GROUP BY 1
