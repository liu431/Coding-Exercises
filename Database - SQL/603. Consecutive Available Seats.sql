# Write your MySQL query statement below
with joined_tbl as (
    select C1.seat_id as s1, C2.seat_id as s2
    from Cinema C1
    join Cinema C2 on C1.seat_id + 1 = C2.seat_id and C1.free = 1 and C2.free = 1)

select s1 as seat_id
from joined_tbl
union
select s2
from joined_tbl
order by 1

# simplier approach
select distinct c1.seat_id
from cinema c1 join cinema c2
on abs(c2.seat_id-c1.seat_id)=1
and c1.free=1 and c2.free=1
order by c1.seat_id
