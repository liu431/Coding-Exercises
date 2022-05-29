# Write your MySQL query statement below
# Report the number of calls and the total call duration between each pair of distinct persons (person1, person2) where person1 < person2
# Use CASE WHEN to switch between p1 and p2 if p1>p2
# Could also use if(from_id > to_id, to_id, from_id) as from_id, if(from_id > to_id, from_id, to_id) as to_id
SELECT 
CASE WHEN from_id < to_id THEN from_id ELSE to_id END AS person1, 
CASE WHEN from_id < to_id THEN to_id ELSE from_id END AS person2, 
COUNT(*) AS call_count, SUM(duration) AS total_duration
FROM Calls
GROUP BY person1, person2
