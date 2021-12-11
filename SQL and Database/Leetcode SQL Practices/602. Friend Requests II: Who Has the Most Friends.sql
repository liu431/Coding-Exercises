# Write your MySQL query statement below
# Find the people who have the most friends and the most friends number
SELECT id, COUNT(*) AS num
FROM
# List of all requester_id and accepter_id
(SELECT requester_id AS id FROM RequestAccepted 
UNION ALL
SELECT accepter_id AS id FROM RequestAccepted) t
GROUP BY id
ORDER BY num DESC
LIMIT 1

