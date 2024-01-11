select 
month, 
country, 
count(id) as "trans_count", 
sum(amount) as "trans_total_amount",
sum(if(state="approved",1,0)) as "approved_count",
sum(approved_amount) as "approved_total_amount"
from
(select 
id, country, state, amount, 
date_format(trans_date,"%Y-%m") as "month",
case 
    when state = "approved" then amount
    else 0 
    end 
    as "approved_amount"
from transactions) as t1 
group by month, country  ; 