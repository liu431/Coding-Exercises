# Write your MySQL query statement below
select 
    artist,
    count(id) as occurrences
from Spotify
group by 1
order by 2 desc, 1
