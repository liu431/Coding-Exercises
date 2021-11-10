# Use LAG and LEAD to calculate the diff between current row with previous and next rows
with diff as 
(select log_id, 
 ifnull(log_id - LAG(log_id, 1) OVER (order by log_id), 0) as lagdiff,
 ifnull(log_id - LEAD(log_id, 1) OVER (order by log_id), 0) as leaddiff
from Logs),
# Get the IDs which indicate the start of a continuous range
startid as 
(select log_id as start_id, row_number() OVER (order by log_id) as id from diff
where lagdiff != 1),
# Get the IDs which indicate the end of a continuous range
endid as 
(select log_id as end_id, row_number() OVER (order by log_id) as id from diff
where leaddiff != -1)
# Join the start_id and end_id
select start_id, end_id
from startid
left join endid
on startid.id=endid.id
