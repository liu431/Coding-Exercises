# Write your MySQL query statement below
# low-quality if the like percentage of the problem (number of likes divided by the total number of votes) is strictly less than 60%
SELECT problem_id
FROM Problems
WHERE likes/(likes + dislikes) < 0.6
ORDER BY problem_id
