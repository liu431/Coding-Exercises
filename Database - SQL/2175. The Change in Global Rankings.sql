# Write your MySQL query statement below
# Calculate the change in the global rankings after updating each team's points.

## Calculate ranks before and after the changes
with ranks as 
(select 
    T.team_id, 
    T.name, 
    rank() over (order by points desc, name) as rank_old,
    rank() over (order by points + points_change desc, name) as rank_new
from TeamPoints T 
join PointsChange P using (team_id))

## Report rank_diff
select 
    team_id,
    name,
    (cast(rank_old as signed) - cast(rank_new as signed)) as rank_diff
from ranks
