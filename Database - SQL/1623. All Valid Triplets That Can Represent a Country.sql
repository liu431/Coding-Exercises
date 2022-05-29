# Write your MySQL query statement below
# Find all the possible triplets representing the country under the given constraints
SELECT A.student_name AS member_A, B.student_name AS member_B, C.student_name AS member_C
FROM SchoolA A
# Join the tables of 3 schools together conditional on students' names and IDs are pairwise distinct
JOIN SchoolB B  ON A.student_id != B.student_id AND A.student_name != B.student_name
JOIN SchoolC C ON A.student_id != C.student_id AND A.student_name != C.student_name
AND B.student_id != C.student_id AND B.student_name != C.student_name
