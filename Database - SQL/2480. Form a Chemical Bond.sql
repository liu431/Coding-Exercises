# Write your MySQL query statement below
select E1.symbol as metal, E2.symbol as nonmetal
from Elements E1, Elements E2
where E1.type = 'Metal' and E2.type = 'Nonmetal'
