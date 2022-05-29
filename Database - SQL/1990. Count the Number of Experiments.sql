# Write your MySQL query statement below

## Cartesian join the table to itself
WITH platforms AS (
SELECT 'IOS' AS platform UNION
SELECT 'Android' AS platform UNION
SELECT 'Web' AS platform),

experi AS
(SELECT 'Reading' AS experiment_name UNION
SELECT 'Sports' AS experiment_name UNION
SELECT 'Programming' AS experiment_name),

PAIRS AS
(SELECT * FROM platforms, experi)

SELECT P.platform, P.experiment_name, COUNT(DISTINCT experiment_id) num_experiments
FROM PAIRS P
LEFT JOIN Experiments E USING(platform, experiment_name)
GROUP BY 1, 2
ORDER BY 1, 2
