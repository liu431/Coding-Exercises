# Write your MySQL query statement below
## Exam table is accumulative
## Find the score with student_cpunt that is closest, but smaller than capacity

# with compared_tbl as (
#     select 
#         school_id,
#         capacity,
#         score,
#         student_count,
#         rank() over (partition by school_id order by student_count desc, score) as rk 
#     from Schools S
#     left join Exam E on S.capacity >= E.student_count)

# select 
#     school_id, 
#     coalesce(score, -1) as score
# from compared_tbl
# where rk = 1

select 
    school_id, 
    coalesce(min(score), -1) as score
from Schools 
left join Exam on capacity >= student_count
group by school_id
