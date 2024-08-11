with cte as 
(select stock_name, 
        case 
            when operation = "Buy" then -price
            when operation = "Sell" then price
            end 
        as "price"
        from stocks)

select stock_name, sum(price) as "capital_gain_loss"
from cte 
group by stock_name  ; 