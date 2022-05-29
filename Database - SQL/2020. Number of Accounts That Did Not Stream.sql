# Write your MySQL query statement below
# Report the number of accounts that bought a subscription in 2021 but did not have any stream session
## Use NOT IN to filter not the ones who didn't have any stream session
## USE YEAR() to find the ones with subscriptions in 2021
SELECT COUNT(account_id) AS accounts_count
FROM Subscriptions
WHERE YEAR(start_date) <= 2021 AND YEAR(end_date)>=2021 AND account_id NOT IN (SELECT account_id FROM Streams WHERE Year(stream_date) = 2021)
