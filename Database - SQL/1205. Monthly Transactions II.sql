# 11/25/21
# Construct new table by unioning two tables
WITH TBL AS
(SELECT T.id, T.country, 'chargeback' AS state, T.amount, C.trans_date
FROM Chargebacks AS C LEFT JOIN Transactions AS T ON C.trans_id = T.id
UNION ALL
SELECT * FROM transactions WHERE state = 'approved'
)
# Output aggregated results
SELECT LEFT(trans_date, 7) AS month, country,
    SUM(state = 'approved') AS approved_count,
    SUM(amount * (state = 'approved')) AS approved_amount,
    SUM(state = 'chargeback') AS chargeback_count,
    SUM(amount * (state = 'chargeback')) AS chargeback_amount
FROM TBL
GROUP BY LEFT(trans_date, 7), country


# 1/8/22
# Find for each month and country: the number of approved transactions and their total amount, the number of chargebacks, and their total amount.
## New table: left join grouped chargebacks to grouped transactions
## Use CASE WHEN and SUM to group by month and country

WITH approved_tbl AS (SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month, 
                        country,
                        COUNT(*) AS approved_count,
                        SUM(amount) AS approved_amount
                        FROM Transactions
                        WHERE state = 'approved'
                        GROUP BY 1, 2),
                        
chargeback_tbl AS (SELECT DATE_FORMAT(C.trans_date, '%Y-%m') AS month, country,
                    COUNT(*) AS chargeback_count, SUM(amount) AS chargeback_amount
                    FROM Chargebacks C
                    LEFT JOIN Transactions ON C.trans_id = Transactions.id
                    GROUP BY 1, 2),
                    
index_tbl AS (SELECT month, country
                FROM approved_tbl
                UNION
                SELECT month, country
                FROM chargeback_tbl)
                
SELECT month, 
        country, 
        COALESCE(approved_count, 0) approved_count,
        COALESCE(approved_amount, 0) approved_amount,
        COALESCE(chargeback_count, 0) chargeback_count,
        COALESCE(chargeback_amount, 0) chargeback_amount
FROM index_tbl
LEFT JOIN approved_tbl USING (month, country)
LEFT JOIN chargeback_tbl USING (month, country)
