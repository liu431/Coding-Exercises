# Write your MySQL query statement below
# Generate a report of period_state for each continuous interval of days in the period from 2019-01-01 to 2019-12-31
## Combine Failed and Succeeded, create rank, and sort
## Use overall_rank  - rk to indicate whether the days are in the same state group
## Group by different state group (state and flag)
# Ref: https://leetcode.com/problems/report-contiguous-dates/discuss/835526/Mysql-window-function-easy-to-understand


            
WITH agg_tbl AS (SELECT dates, state, (RANK() OVER (ORDER BY dates) - rk) AS flag
                FROM (SELECT fail_date AS dates, 'failed' AS state, RANK() OVER (ORDER BY fail_date) AS rk
                    FROM Failed
                    WHERE YEAR(fail_date) = 2019
                    UNION
                    SELECT success_date AS dates, 'succeeded' AS state, RANK() OVER (ORDER BY success_date) AS rk
                    FROM Succeeded
                    WHERE YEAR(success_date) = 2019
                    ORDER BY dates) t)
                    
SELECT state AS 'period_state', MIN(dates) AS start_date, MAX(dates) AS end_date
FROM agg_tbl 
GROUP BY state, flag
ORDER BY start_date
