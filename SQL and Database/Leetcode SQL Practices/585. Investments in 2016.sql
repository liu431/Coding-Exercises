# Write your MySQL query statement below
# Report the sum of all total investment values in 2016 tiv_2016, for all policyholders who: have the same tiv_2015 value as one or more other policyholders, and are not located in the same city like any other policyholder (i.e., the (lat, lon) attribute pairs must be unique).
## Condition 1: tiv_2015 counts >= 2
## Condition 2: (lat, lon) count = 1
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016 
FROM Insurance
WHERE tiv_2015 IN (SELECT tiv_2015 FROM Insurance GROUP BY tiv_2015 HAVING COUNT(*) > 1)
AND (lat, lon) IN (SELECT lat, lon FROM Insurance GROUP BY lat, lon HAVING COUNT(*) = 1)
