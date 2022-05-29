# Write your MySQL query statement below
# Select the team_id, team_name and num_points of each team in the tournament after all described matches
## From Matches, calculate points for host and guest teams
## Flatten the Matches table and aggregate by teams
## Left join to Teams

WITH point_tbl AS (SELECT *, 
                    CASE WHEN (host_goals > guest_goals) THEN 3
                    WHEN (host_goals = guest_goals) THEN 1
                    ELSE 0 END AS host_points,
                    CASE WHEN (host_goals > guest_goals) THEN 0
                    WHEN (host_goals = guest_goals) THEN 1
                    ELSE 3 END AS guest_points
                    FROM Matches),
                    
point_total AS (SELECT team_id, SUM(num_points) AS num_points                
FROM (SELECT host_team as team_id, host_points as num_points
        FROM point_tbl
        UNION ALL
        SELECT guest_team as team_id, guest_points as num_points
        FROM point_tbl) t
GROUP By 1)

SELECT Teams.team_id, Teams.team_name, COALESCE(num_points, 0) AS num_points
FROM Teams
LEFT JOIN point_total USING (team_id)
ORDER BY 3 DESC, 1
