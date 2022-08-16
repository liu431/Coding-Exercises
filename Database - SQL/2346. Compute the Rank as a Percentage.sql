# Write your MySQL query statement below
## percentage: (student_rank_in_the_department - 1) * 100 / (the_number_of_students_in_the_department - 1)

with tbl as
(select 
    student_id, 
    department_id,
    rank() over (partition by department_id order by mark desc) as student_rank_in_the_department,
    count(student_id) over (partition by department_id) as the_number_of_students_in_the_department
from Students)

select 
    student_id, 
    department_id,
    round(coalesce((student_rank_in_the_department - 1) * 100 / (the_number_of_students_in_the_department - 1), 0), 2) as percentage
from tbl
    
