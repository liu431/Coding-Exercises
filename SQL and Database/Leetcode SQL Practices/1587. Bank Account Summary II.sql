# Write your MySQL query statement below
# Report the name and balance of users with a balance higher than 10000
SELECT name, SUM(amount) AS balance
FROM Transactions
JOIN Users USING (account)
GROUP BY account
HAVING balance > 10000
