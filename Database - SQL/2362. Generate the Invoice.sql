# Write your MySQL query statement below
## Create purchase table with total prices
## Calculate the invoice total prices by grouping invoice_id and summing prices
## Find the invoice_id with the highest price (limit by 1)
## Select the purchase details with this invoice_id

with purchases_with_prices as
(
select invoice_id, product_id, quantity, (quantity * price) as price
from Purchases
join Products using (product_id)
),

invoice_with_highest_prices as
(select invoice_id, sum(price)
from purchases_with_prices
group by 1
order by 2 desc, 1
limit 1)

select product_id, quantity, price
from purchases_with_prices
where invoice_id = (select invoice_id from invoice_with_highest_prices)
