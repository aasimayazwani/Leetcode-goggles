# Write your MySQL query statement below
select transaction_id
from 
(select *, dense_rank() over (partition by day order by amount desc) as "ranking"
from
    (select transaction_id,amount,date_format(day,"%Y-%m-%d") as "day"
    from transactions) 
    as t1 ) as t2 
where ranking = 1
order by transaction_id asc  ; 