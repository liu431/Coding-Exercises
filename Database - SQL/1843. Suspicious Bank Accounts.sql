# Write your MySQL query statement below
# Report the IDs of all suspicious bank accounts.
## Group transactions by id and month to get total income
## Keep the ids that are suspicious for 2+ consecutive months
## 2+ consecutive months: mon diff is 1 or -11 (Dec and Jan of next year case)

WITH AGG AS (SELECT account_id, MONTH(day) AS YM, 
                SUM(CASE WHEN type='Creditor' THEN amount ELSE 0 END) AS total, max_income
            FROM Transactions
            LEFT JOIN Accounts USING (account_id)
            GROUP BY 1, 2
            HAVING total > max_income
            ORDER BY 1, 2)

SELECT DISTINCT account_id
FROM (SELECT account_id, YM - LAG(YM) OVER (PARTITION BY account_id) AS MonDiff
        FROM AGG) t
WHERE MonDiff IN (1, -11)
