# Write your MySQL query statement below
## Report the median of all the numbers in the database after decompressing the Numbers table
## First, find median index of num length
## Second, find the num with frequency equals or smaller than median index


WITH cum AS (
    SELECT *, SUM(frequency) OVER (ORDER BY num) AS cum_sum
    FROM Numbers),
even_case AS (SELECT  MIN(num) AS num
            FROM cum
            WHERE cum_sum >= (SELECT SUM(frequency)/2 FROM Numbers)
            UNION ALL
            SELECT MIN(num) AS num
            FROM cum
            WHERE cum_sum >= (SELECT (SUM(frequency)/2) + 1 FROM Numbers)
            ),
odd_case AS (SELECT *
            FROM cum
            WHERE cum_sum >= (SELECT (SUM(frequency)+1) / 2 FROM Numbers)
            LIMIT 1)
SELECT CASE WHEN mod((SELECT SUM(frequency) FROM Numbers), 2)=0 THEN (SELECT AVG(num) FROM even_case) 
        ELSE (SELECT num FROM odd_case) END AS median

