# Write your MySQL query statement below
# Find out the current balance of all users and check whether they have breached their credit limit
## Get credit changes for each user from Transactions
WITH Trans AS (SELECT user_id, SUM(amt) AS amount 
FROM 
(SELECT paid_by AS user_id, -amount AS amt
FROM Transactions
## USE UNION ALL to keep all transactions
UNION ALL
SELECT paid_to AS user_id, amount AS amt
FROM Transactions) t
GROUP BY user_id)

SELECT U.user_id, user_name, credit + IFNULL(amount, 0) AS credit,
CASE WHEN credit + IFNULL(amount, 0) > 0 THEN 'No'
ELSE 'Yes' END AS credit_limit_breached
FROM Users U
LEFT JOIN Trans USING (user_id)
