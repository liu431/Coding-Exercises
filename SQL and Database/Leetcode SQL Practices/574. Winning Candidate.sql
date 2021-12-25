# Write your MySQL query statement below
# Report the name of the winning candidate (i.e., the candidate who got the largest number of votes
SELECT name
FROM Vote
JOIN Candidate ON Candidate.id = Vote.candidateId
GROUP BY candidateId
ORDER BY COUNT(*) DESC
LIMIT 1
