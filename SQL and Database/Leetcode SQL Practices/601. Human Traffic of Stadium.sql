# Write your MySQL query statement below
# Display the records with three or more rows with consecutive id's, and the number of people is greater than or equal to 100 for each

## use lag() and lead() to get 2 of the preceding and succeeding people values
WITH AdjTbl AS 
(SELECT *, 
LEAD(people, 1) OVER () AS lead1,
LEAD(people, 2) OVER () AS lead2,
LAG(people, 1) OVER () AS lag1,
LAG(people, 2) OVER() AS lag2
From Stadium)

## Export results
SELECT id, visit_date, people
FROM AdjTbl
WHERE people >= 100 AND
## Any qualifying row will met one of the three conditions:
## 1. 2 succeeding people have over 100
## 2. 1 preceding and 1 succeeding people have over 100
## 3. 2 preceding people have over 100
((lead1 >= 100 AND lead2 >= 100)
 OR (lag1 >= 100 AND lead1 >= 100)
 OR (lag1 >= 100 AND lag2 >= 100))
