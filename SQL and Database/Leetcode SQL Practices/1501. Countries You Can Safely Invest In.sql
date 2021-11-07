# Join tables to get the average call duration of the calls in each country 
select Co.name as country from Calls C
join Person P on C.caller_id=P.id or C.callee_id=P.id
join Country Co on Co.country_code=left(P.phone_number,3)
group by Co.name
# Filter: strictly greater than the global average call duration
having avg(duration) > (select avg(duration) from Calls)
