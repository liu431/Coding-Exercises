# Write your MySQL query statement below
# Find how many users visited the bank and didn't do any transactions, how many visited the bank and did one transaction and so on.

## Join Visits and Transactions and group by user)id and transaction_date
## USE ROW_NUMBER() to get num sequence

WITH tbl AS (SELECT trans_cts, COUNT(*) AS visits_counts
            FROM (SELECT V.user_id, V.visit_date, COALESCE(trans_cts, 0) AS trans_cts
                FROM Visits V
                LEFT JOIN (SELECT *, 
                           COUNT(transaction_date) AS trans_cts 
                           FROM Transactions
                            GROUP BY 1, 2) t
                ON t.user_id = V.user_id AND t.transaction_date = V.visit_date) agg
            GROUP BY 1),
            
row_nums AS (SELECT ROW_NUMBER() OVER () as rn 
             FROM Transactions 
             UNION 
             SELECT 0) 
            
SELECT rn AS transactions_count, COALESCE(visits_counts, 0) AS visits_count
FROM row_nums
LEFT JOIN tbl ON tbl.trans_cts = row_nums.rn
WHERE rn <= (SELECT MAX(trans_cts) FROM tbl)
ORDER BY 1
