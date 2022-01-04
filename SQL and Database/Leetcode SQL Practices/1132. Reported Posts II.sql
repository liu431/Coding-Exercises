# Write your MySQL query statement below
# Find the average daily percentage of posts that got removed after being reported as spam, rounded to 2 decimal places
## Need columns: day, post counts, spam counts
## Calculate the average of removal percentage of spam posts
SELECT ROUND(AVG(percent), 2) AS average_daily_percent 
FROM (SELECT action_date,  
            100* COUNT(DISTINCT Removals.post_id)/COUNT(DISTINCT Actions.post_id) AS percent
        FROM Actions
        LEFT JOIN Removals USING (post_id)
        WHERE extra = 'spam'
        GROUP BY action_date) t
