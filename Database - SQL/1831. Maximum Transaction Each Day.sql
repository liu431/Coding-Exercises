# Write your MySQL query statement below
# Report the IDs of the transactions with the maximum amount on their respective day
## Use RANK() to assign rank for transaction amounts by day
## Return ids with rank 1
SELECT transaction_id
FROM 
(SELECT transaction_id, RANK() OVER (PARTITION BY DATE_FORMAT(day, '%Y-%m-%d') ORDER BY amount DESC) AS amt_rank FROM Transactions) t
WHERE amt_rank = 1
ORDER BY transaction_id










