# Write your MySQL query statement below
# two indexes: 1st rank_num for user_id within group; 2st code number for ordering gender
# order by the two ranks

select user_id, gender
from 
(select 
    user_id, 
    gender, 
    rank() over (partition by gender order by user_id) as id_rank, 
    case when (gender='female') then 0
    when gender='other'then 1
    else 2 end as gender_code
from Genders
order by 3, 4) G
