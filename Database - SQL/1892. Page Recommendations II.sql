# Write your MySQL query statement below
with pairs as (
    select user1_id, user2_id from Friendship
    union
    select user2_id, user1_id from Friendship
),

all_likes as (
select 
    F.user1_id as user_id,
    L.page_id,
    count(*) as friends_likes
from pairs F
join Likes L on F.user2_id = L.user_id 
group by 1, 2
order by 1),

user_liked_pages as (
    select 
        user_id,
        group_concat(concat('+', page_id, '+')) as liked_pages
    from Likes
    group by 1
)

select 
    A.user_id,
    A.page_id,
    friends_likes
from all_likes A
join user_liked_pages B on A.user_id = B.user_id
where B.liked_pages not like concat('%', '+', A.page_id, '+', '%')
