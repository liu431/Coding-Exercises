# Write your MySQL query statement below
# 1. group by to get voters' number of votes
# 2. calculate the split scores
# 3. link back to candidate
# 4. group by candidate to get sum

with vote_score as (
  select 
    voter, 
    case when count(distinct candidate) > 0 then 1/count(distinct candidate) else 0 end as cts
  from votes
  group by 1),

candidate_rank as(
select candidate, rank() over (order by sum(cts) desc) rks
from votes
left join vote_score using (voter)
group by candidate
order by 2)

select candidate
from candidate_rank
where rks = 1
order by 1
