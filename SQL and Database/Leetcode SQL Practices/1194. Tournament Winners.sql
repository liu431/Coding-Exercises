# Write your MySQL query statement below
# Find the winner in each group. The winner in each group is the player who scored the maximum total points within the group.

## Get aggregated scores from Matches
## Left join to Players
## Find max in each group by rank

WITH agg_point AS (SELECT player_id, SUM(score) AS total
                    FROM(
                        SELECT first_player AS player_id, first_score AS score
                        FROM Matches
                        UNION ALL 
                        SELECT second_player AS player_id, second_score AS score
                        FROM Matches) t
                    GROUP BY 1)
SELECT group_id, player_id
FROM (SELECT group_id, player_id, RANK() OVER (PARTITION BY group_id ORDER BY total DESC, player_id) AS point_rank
        FROM Players
        LEFT JOIN agg_point USING (player_id)) t
WHERE point_rank = 1

