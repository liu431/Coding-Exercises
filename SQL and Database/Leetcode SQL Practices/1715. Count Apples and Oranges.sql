# Write your MySQL query statement below
# Count the number of apples and oranges in all the boxes
## Use IFNULL() for boxes without chests
SELECT SUM(B.apple_count) + IFNULL(SUM(C.apple_count),0) AS apple_count,
SUM(B.orange_count) + IFNULL(SUM(C.orange_count),0) AS orange_count
FROM Boxes B
LEFT JOIN Chests C USING (chest_id)
