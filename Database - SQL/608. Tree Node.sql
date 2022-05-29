select id, 
# Root: it does not have a parent node at all
case when p_id is null then 'Root'
# Inner: it is the parent node of some nodes, and it has a not NULL parent itself.
when id in (select p_id from Tree) then 'Inner'
# Leaf: rest of the cases other than above two
else 'Leaf' end as type
from Tree
order by id
