# Write your MySQL query statement below
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
