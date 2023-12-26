with cte as
(select account_id, day, balance_amount from 
(select *, 
case when type = "Deposit" then amount 
     when type ="Withdraw" then -amount
end 
as "balance_amount"
from transactions ) as t1 )


select account_id, day, sum(balance_amount) over (partition by account_id  order by day)
as "balance"
from cte 
order by account_id asc, day asc ;