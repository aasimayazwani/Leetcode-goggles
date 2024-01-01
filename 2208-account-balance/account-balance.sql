with cte as
(select account_id, day, 
case
    when type = "Deposit" then +amount 
    when type = "Withdraw" then -amount
    end 
    as "balance"
    from transactions )


select account_id, day, sum(balance) over (partition by account_id order by day) as "balance"
from cte 
order by account_id asc, day asc ; 
