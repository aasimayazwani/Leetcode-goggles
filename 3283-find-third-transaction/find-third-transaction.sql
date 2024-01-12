with cte as 
(select user_id, spend, transaction_date, ranking from
(select *,
dense_rank() over (partition by user_id order by transaction_date asc) as 
"ranking" 
from transactions
order by transaction_date) as t0
where ranking <= 3 )



select distinct t3.user_id, 
t3.spend as "third_transaction_spend",
t3.transaction_date as "third_transaction_date"
 from cte as t1, cte as t2, cte as t3 
where 
t1.user_id = t2.user_id and 
t2.user_id = t3.user_id and 
t1.spend < t3.spend and 
t2.spend < t3.spend and 
t1.ranking < t2.ranking and 
t2.ranking < t3.ranking 
order by t3.user_id asc ;