# Write your MySQL query statement below
# Get book IDs and copies that sold in the last year
with sales as (select book_id, sum(quantity) as copies
from Orders O 
where DATEDIFF('2019-06-23', dispatch_date) < 365
group by book_id)

# Output results
select B.book_id, name
from Books B
left join sales on sales.book_id=B.book_id
# Condition 1: sold less than 10 copies in the last year
# Conditon 2: exclude books that have been available for less than one month from today
where ifnull(copies, 0) < 10 and DATEDIFF('2019-06-23', available_from) > 31
