# Write your MySQL query statement below
# Fact table: Sales; Dim tables: Salesperson and Customer
with agg_sales as
(select salesperson_id, sum(price) as total
from Sales
left join Customer using (customer_id)
left join Salesperson using (salesperson_id)
group by 1)

select salesperson_id, name, coalesce(total, 0) as total
from Salesperson
left join agg_sales using (salesperson_id)
