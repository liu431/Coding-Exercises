# Write your MySQL query statement below
select left_operand, operator, right_operand,
# Use case when to evaluate values
# Use if(value, 'true', 'false') to convert boolean to string
case when operator='>' then if(V.value>V2.value, 'true', 'false')
when operator='=' then if(V.value=V2.value, 'true', 'false')
else if(V.value<V2.value, 'true', 'false') end as value
from Expressions E
# Get value for left_operand
left join Variables V on V.name=E.left_operand
# Get value for right_operand
left join Variables V2 on V2.name=E.right_operand
