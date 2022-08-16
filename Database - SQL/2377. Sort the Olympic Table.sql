# Write your MySQL query statement below
select country, gold_medals, silver_medals, bronze_medals
from Olympic 
order by 2 desc, 3 desc, 4 desc, 1
