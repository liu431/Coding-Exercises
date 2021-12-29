# Write your MySQL query statement below
## report the shortest distance between any two points from the Point2D table
## Self join ; not include same point
## Find the min
SELECT ROUND(SQRT(MIN((P1.x - P2.x)*(P1.x - P2.x) + (P1.y - P2.y)*(P1.y - P2.y))), 2) AS shortest
FROM Point2D P1, Point2D P2
WHERE P1.x != P2.x OR P1.y != P2.y
