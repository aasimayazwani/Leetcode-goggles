select transaction_id
from 
(select transaction_id, 
dense_rank() over (partition by day_value order by amount desc) as "ranking"
from 
(select transaction_id, date_format(day,"%Y-%m-%d") as "day_value", 
amount
from transactions) as t1) as t2 
where 
ranking = 1 
order by transaction_id asc ;