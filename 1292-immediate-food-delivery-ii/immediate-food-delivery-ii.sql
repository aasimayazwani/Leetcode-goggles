# Write your MySQL query statement below
with cte as 
(select * from 
(select *, dense_rank() over (partition by customer_id order by order_date asc) as 
"counting"
from delivery) as t1 
where counting = 1 )


select round(count(delivery_id)*100/(select count(delivery_id) from cte),2)
as "immediate_percentage"
from cte  
where order_date = customer_pref_delivery_date ; 