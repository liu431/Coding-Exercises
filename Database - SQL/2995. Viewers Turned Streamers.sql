# Write your MySQL query statement below
with rk as (
        select 
            user_id,
            session_id,
            session_type,
            row_number() over (partition by user_id order by session_start) as ss_rk
        from Sessions
    ),
    fl as (
        select 
            user_id
        from rk
        where session_type = 'Viewer' and ss_rk = 1
    )
select 
    user_id,
    sum(session_type = 'Streamer') as sessions_count
from sessions
where user_id in (select user_id from fl)
group by 1
having sessions_count > 0
order by 2 desc, 1 desc
