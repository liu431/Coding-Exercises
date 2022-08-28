# Write your MySQL query statement below
# Write an SQL query to report the name and the mail of all interview candidates. A user is an interview candidate if at least one of these two conditions is true:

# 1. The user won any medal in three or more consecutive contests.
# 2. The user won the gold medal in three or more different contests (not necessarily consecutive).

with flatlist as 
(select gold_medal as id, contest_id
from Contests
union
select silver_medal as id , contest_id
from Contests
union
select bronze_medal as id , contest_id
from Contests),

id_rank as 
(select 
    id,
    contest_id,
    rank() over (partition by id order by contest_id) as rk
from flatlist),

candidiate_id as
(select id
from id_rank
group by 1, contest_id - rk
having count(*) >= 3
union
# 3+ gold medal
select gold_medal as id
from contests
group by 1
having count(contest_id) >= 3)

select name, mail
from Users
where user_id in (select * from candidiate_id)
