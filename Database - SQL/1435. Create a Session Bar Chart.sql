# Write your MySQL query statement below
# Convert duration to bins
WITH bin_tbl AS (SELECT 
CASE WHEN duration/60 >=0 AND duration/60 < 5 THEN '[0-5>'
WHEN  duration/60 >= 5 AND duration/60 < 10 THEN '[5-10>'
WHEN duration/60 >= 10 AND duration/60 < 15 THEN '[10-15>'
ELSE '15 or more' END AS bin
FROM Sessions),

# Aggregate bins
bin_cts AS
(SELECT bin, COUNT(*) AS total FROM bin_tbl GROUP BY bin),

# Create bin list; Otherwise, bins with 0 count will be missing in result
bin_list AS (SELECT '[0-5>' AS bin
UNION 
SELECT '[5-10>'
UNION 
SELECT '[10-15>'
UNION 
SELECT '15 or more')

# Count the number of sessions on it
SELECT bin_list.bin, IFNULL(total, 0) AS total
FROM bin_list
LEFT JOIN bin_cts ON bin_list.bin = bin_cts.bin
