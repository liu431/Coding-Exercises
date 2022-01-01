# Write your MySQL query statement below
# Report the statistics of the league

## CTE1: assign points in the matches
WITH Matches_Points AS (SELECT *,
CASE WHEN home_team_goals > away_team_goals THEN 3
WHEN home_team_goals = away_team_goals THEN 1
ELSE 0 END AS home_team_points,
CASE WHEN home_team_goals < away_team_goals THEN 3
WHEN home_team_goals = away_team_goals THEN 1
ELSE 0 END AS away_team_points
FROM Matches),

## CTE2: flatten matches table to a list
AllTeams AS (SELECT home_team_id, home_team_points, home_team_goals, away_team_goals
FROM Matches_Points
UNION ALL
SELECT away_team_id, away_team_points, away_team_goals, home_team_goals
FROM Matches_Points)

## Group by teams and get totals
SELECT 
    team_name, 
    COUNT(*) AS matches_played, 
    SUM(home_team_points) AS points, 
    SUM(home_team_goals) AS goal_for, 
    SUM(away_team_goals) AS goal_against,
    SUM(home_team_goals) -  SUM(away_team_goals) AS goal_diff
FROM AllTeams 
JOIN Teams ON Teams.team_id = AllTeams.home_team_id
GROUP BY team_name
ORDER BY points DESC, goal_diff DESC, team_name





