# Write your MySQL query statement below
## Use rank() to rank the activity time
## Get count of each user's activities
## Add the rank and cts to the main table
## If count > 1: return the second most recent activity of each user
## If count = 1: return that one


with detailed_activity as
(select *, 
    rank() over (partition by username order by endDate desc) as act_rank,
    count(*) over (partition by username) as cts 
from UserActivity
)

select username, activity, startDate, endDate
from detailed_activity
where cts = 1 or act_rank = 2




