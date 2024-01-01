# Write your MySQL query statement below
select stock_name, sum(total) as "capital_gain_loss" from
(select stock_name, 
case 
    when operation = "Buy" then -price
    when operation = "Sell" then price
    end 
    as "total"
    from stocks) as t1 
group by stock_name 
  ;  