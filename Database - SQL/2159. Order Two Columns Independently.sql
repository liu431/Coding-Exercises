# Write your MySQL query statement below
## Use CTE to get ordered lists and combine them with same row numbers
with col1 as (
    select first_col, row_number () over (order by first_col) as ind
    from Data
),
col2 as (
    select second_col, row_number () over (order by second_col desc) as ind
    from Data
)

select 
    first_col,
    second_col
from col1
join col2 using (ind)
