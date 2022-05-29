# Write your MySQL query statement below
# Report the IDs of the candidates who have at least two years of experience and the sum of the score of their interview rounds is strictly greater than 15
SELECT candidate_id 
FROM Candidates
JOIN (SELECT interview_id, SUM(score) AS tscore FROM Rounds GROUP BY interview_id) R USING (interview_id)
WHERE tscore > 15 AND years_of_exp >= 2
