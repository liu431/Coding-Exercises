# Write your MySQL query statement below
# Report the question that has the highest answer rate
## answer rate for a question is the number of times a user answered the question by the number of times a user showed the question.
## Subquery: find all ids, show/answer counts by question
WITH CTS AS (SELECT question_id,
SUM(CASE WHEN action='show' THEN 1 ELSE 0 END) AS ShowCts, 
SUM(CASE WHEN action='answer' THEN 1 ELSE 0 END) AS AnsCts
FROM SurveyLog
GROUP BY question_id)

## Rank all the rates (answer/(answer+show)) and return the max one
SELECT question_id AS survey_log
FROM (SELECT question_id, DENSE_RANK() OVER (ORDER BY (AnsCts/(AnsCts + ShowCts)) DESC) AS raterank
FROM CTS) t
WHERE raterank = 1
ORDER BY question_id
LIMIT 1



