# Get the ID list of user 1's friends
with friendid as (select user1_id as user_id from Friendship where user2_id=1
union 
select user2_id from Friendship where user1_id=1)
# Get the page ID
select distinct page_id as recommended_page 
from Likes
# Filter 1: using the pages that user 1's friends liked
where user_id IN (select * from friendid) and 
# Filter 2: should not recommend pages user 1 already liked
page_id NOT IN (select page_id from Likes where user_id =1)
