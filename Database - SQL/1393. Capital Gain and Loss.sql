select stock_name,
# sum over transaction prices
sum(case when operation='Sell' then price
else -1*price end) as capital_gain_loss 
from Stocks
group by stock_name
