# Write your MySQL query statement below
select stock_name, sum(price) as "capital_gain_loss"
from
(select stock_name, 
case 
    when operation = "Buy" then -price
    when operation = "Sell" then price
end 
as "price"
from stocks) as t1 
group by stock_name 