# Write your MySQL query statement below
# use rank() to get maximum recorded degree in each city
with t as 
(select city_id, day, degree, rank() over (partition by city_id order by degree desc, day) as degree_rank
from Weather)
select city_id, day, degree
from t
where degree_rank = 1
