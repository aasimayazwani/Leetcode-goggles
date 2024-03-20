select account_id, day, balance
from 
(select account_id, day, sum(amount) over (partition by account_id order by day asc) as "balance"
from 
(select   
account_id, day, 
case 
    when type = "Deposit" then amount
    when type = "Withdraw" then -amount
end
as "amount"
from transactions) as t1 ) as t2 
order by account_id asc , day asc ;