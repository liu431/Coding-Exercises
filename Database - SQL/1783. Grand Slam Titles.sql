# Write your MySQL query statement below
# Report the number of grand slam tournaments won by each player
## Aggregate cts by player from Championships 
WITH tbl AS 
(SELECT Wimbledon As player_id, COUNT(*) AS grand_slams_count 
FROM
(SELECT Wimbledon FROM Championships 
UNION ALL 
SELECT Fr_open FROM Championships 
UNION ALL
SELECT US_open FROM Championships 
UNION ALL
SELECT Au_open FROM Championships) t
GROUP BY Wimbledon)
## Get result
SELECT Players.player_id, player_name, grand_slams_count
FROM Players
JOIN tbl ON tbl.player_id = Players.player_id
