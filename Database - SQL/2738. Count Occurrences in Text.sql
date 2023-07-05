# Write your MySQL query statement below
select 'bull' as "word", count(1) as "count"
from Files
where RegExp_Like(content, '([^a-z])bull([^a-z])')
union
select 'bear' as "word", count(1) as "count"
from Files
where RegExp_Like(content, '([^a-z])bear([^a-z])')
