# Use SUM() and window function to get the running total for each gender and day
select gender, day, sum(score_points) over (partition by gender order by day) as total
from Scores
group by gender, day
