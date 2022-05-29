# Write your MySQL query statement below
# Numerator: number of players that logged in for at least two consecutive days starting from their first login date
# Denominator: total number of players
select round(count(distinct A1.player_id) / (select count(distinct player_id) from Activity), 2) as fraction
from Activity A1
# Self join: keep only rows that represent first and second login activities
left join 
(select player_id, min(event_date) as first_date from Activity group by player_id) A2 
on A1.player_id = A2.player_id 
where datediff(A1.event_date, A2.first_date) = 1 


