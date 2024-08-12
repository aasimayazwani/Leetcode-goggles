# Write your MySQL query statement below
with cte as 
(select *, dense_rank() over (partition by date order by amount desc) as "ranking"
from
(select transaction_id, 
    date_format(day,"%Y-%m-%d") as "date", 
    amount
    from transactions) as t1) 

select transaction_id from cte 
where ranking = 1 
order by transaction_id asc ; 