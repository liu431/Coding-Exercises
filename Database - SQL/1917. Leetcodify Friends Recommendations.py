# Write your MySQL query statement below
# Write an SQL query to recommend friends to Leetcodify users. We recommend user x to user y if:

# Users x and y are not friends, and
# Users x and y listened to the same three or more different songs on the same day.

## using left join and where to filter out the records in friends, this is faster than running (id1, id2) not in (select id1, id2 from Friendship) and (id1, id2) not in (select id2, id1 from Friendship )
with joined_tbl as
(select 
    distinct L1.user_id as id1,
    L2.user_id as id2,
    L1.day as day,
    L1.song_id as s_id
from Listens L1
join Listens L2 on L1.user_id <> L2.user_id and L1.song_id = L2.song_id and L1.day = L2.day 
group by 1,2,3
having count(distinct L1.song_id ) >= 3)


select distinct id1 as user_id, id2 as recommended_id from joined_tbl
left join 
(select user1_id, user2_id from Friendship
 union 
 select user2_id as user1_id, user1_id as user2_id from Friendship) F
on F.user1_id = joined_tbl.id1 and F.user2_id = joined_tbl.id2
where F.user2_id is null
order by 1
