# Write your MySQL query statement below
select 
    concat(T1.topping_name, ',' , T2.topping_name, ',' , T3.topping_name) as pizza, 
    T1.cost + T2.cost + T3.cost as total_cost 
from Toppings T1 
join Toppings T2 on T1.topping_name < T2.topping_name
join Toppings T3 on T2.topping_name < T3.topping_name
order by 2 desc, 1
