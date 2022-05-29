# Write your MySQL query statement below
# Find the percentage of the users registered in each contest
WITH student_cts AS 
(SELECT COUNT(*) AS cts FROM Users)
SELECT contest_id, ROUND(100 * COUNT(*)/(SELECT cts FROM student_cts), 2)  AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id
