# Write your MySQL query statement below
# Find the total number of users and the total amount spent using the mobile only, the desktop only, and both mobile and desktop together for each date

## Create a flag to indicate whether a user purchased both platforms on a given day
WITH ind AS (SELECT *,
SUM(CASE WHEN platform='mobile' THEN 1 ELSE -1 END) AS flag
FROM Spending
GROUP BY spend_date, user_id),

## Add the flag to Spending
NewS AS (SELECT S.user_id, S.spend_date, (CASE WHEN flag = 0 THEN 'both' ELSE S.platform END) AS platform, S.amount
FROM Spending S
LEFT JOIN ind USING (user_id, spend_date)),

## Create grouping list
grouplist AS 
(SELECT DISTINCT(spend_date), 'desktop' platform FROM Spending
UNION
SELECT DISTINCT(spend_date), 'mobile' platform FROM Spending
UNION
SELECT DISTINCT(spend_date), 'both' platform FROM Spending)

SELECT spend_date, platform, IFNULL(SUM(amount), 0) AS total_amount, IFNULL(COUNT(DISTINCT user_id), 0) AS total_users
FROM grouplist LEFT JOIN NewS USING (spend_date, platform)
GROUP BY spend_date, platform
