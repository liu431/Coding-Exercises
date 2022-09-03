# Write your MySQL query statement below
# report the IDs of the employees that did not work the needed hours.
with hours as
(select 
    employee_id,
    sum(ceiling(timestampdiff(second, in_time, out_time))/3600) as worked_hours
from Logs
group by 1)

select employee_id
from Employees
left join hours using (employee_id)
where needed_hours >= coalesce(worked_hours, 0)
