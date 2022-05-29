# Write your MySQL query statement below
# Find the account_id of the accounts that should be banned from Leetflex. An account should be banned if it was logged in at some moment from two different IP addresses.

## Use self join to find pairs where second login is before first logout and the ip_address are different

SELECT DISTINCT L1.account_id
FROM LogInfo L1
JOIN LogInfo L2 ON L1.account_id = L2.account_id AND L1.ip_address != L2.ip_address AND L1.logout >= L2.login AND L1.login <= L2.login
