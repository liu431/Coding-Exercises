# Write your MySQL query statement below
## A quiet student is the one who took at least one exam and did not score the high or the low score.
## Get the list of student_id who score the high or the low score with rank()
## select student_id from Student where id not in the list

with score_rank as 
(select 
    exam_id, 
    student_id,
    student_name,
    rank() over (partition by exam_id order by score desc) as high,
    rank() over (partition by exam_id order by score asc) as low
from Exam
join Student using (student_id))

select distinct student_id, student_name
from score_rank
where student_id not in
(select distinct student_id
from score_rank
where high = 1 or low = 1)
order by 1

