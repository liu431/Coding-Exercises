# Write your MySQL query statement below
# For each user_id, find out the largest window of days between each visit and the one right after it (or today if you are considering the last visit)

## Impute today's visits into the UserVisits table
With V AS (SELECT DISTINCT user_id, '2021-1-1' AS visit_date
            FROM UserVisits
            UNION
            SELECT * FROM UserVisits),
## Use LAG() to find the windows between visits
WinDays AS (SELECT user_id, DATEDIFF(visit_date, LAG(visit_date) OVER          (PARTITION BY user_id ORDER BY visit_date)) AS windows
        FROM (SELECT user_id, visit_date 
             FROM V 
             ORDER BY 1, 2) t)

## Find the largest window of days for each user
SELECT user_id, MAX(windows) AS biggest_window
FROM WinDays
GROUP BY 1
ORDER BY 1
