# Write your MySQL query statement below
-- Odd seat: self join on s1.id + 1 = s22.id
-- EVen seat: self join s1.id -1 = s2.id

SELECT s1.id, COALESCE(s2.student, s1.student) AS student
FROM Seat s1
LEFT JOIN Seat s2 ON s1.id + 1 = s2.id
WHERE s1.id % 2 = 1
UNION
SELECT s1.id, s2.student AS student
FROM Seat s1
JOIN Seat s2 ON s1.id - 1 = s2.id
WHERE s1.id % 2 = 0
ORDER BY id
