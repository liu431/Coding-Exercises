# Write your MySQL query statement below
# Report the id, the name, and the category of each member.
## conversion rate of a member: (100 * total number of purchases for the member) / total number of visits for the member
## Use Visits and Purchases to get the numbers of purchases and visits
## Join back to Members
## Use CASE WHEN to categorize members

WITH rate_tbl AS (SELECT member_id, 100 * COUNT(charged_amount)/COUNT(visit_date) AS rate
FROM Visits
LEFT JOIN Purchases USING (visit_id)
GROUP BY 1)

SELECT member_id, name,
CASE WHEN rate IS NULL THEN 'Bronze'
WHEN rate >= 80 THEN 'Diamond'
WHEN rate >= 50 AND rate < 80 THEN 'Gold'
WHEN rate < 50 THEN 'Silver' END AS category 
FROM Members
LEFT JOIN rate_tbl USING (member_id)
