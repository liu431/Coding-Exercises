# Write your MySQL query statement below
SELECT
  SUBSTRING_INDEX(email,'@',-1) AS email_domain, count(*) as count
FROM Emails
where email LIKE '%.com'
group by 1
order by 1
