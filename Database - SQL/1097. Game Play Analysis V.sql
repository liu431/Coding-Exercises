# Write your MySQL query statement below
# Report for each install date, the number of players that installed the game on that day, and the day one retention.

## Use rank to filter the records that are first-time installs
## Use self join to get 2 adjacent day record
## Calculate retention rate with records that are installs

WITH rk_tbl AS (SELECT event_date, player_id, RANK() OVER (PARTITION BY player_id ORDER BY event_date) AS rk
FROM Activity)

SELECT A1.event_date AS install_dt, COUNT(A1.player_id) AS installs, ROUND(COUNT(A2.player_id)/ COUNT(A1.player_id), 2) AS Day1_retention
FROM Activity A1
LEFT JOIN Activity A2 ON A1.player_id = A2.player_id AND A1.event_date + 1 = A2.event_date
WHERE (A1.event_date, A1.player_id) IN (SELECT event_date, player_id FROM rk_tbl WHERE rk = 1)
GROUP BY 1
ORDER BY 1
