# Write your MySQL query statement below
with cte as 
(select customer_id, order_date, customer_pref_delivery_date,ranking from 
(select *, dense_rank() over (partition by customer_id order by order_date asc ) as "ranking" from delivery) as t1  ) 

select round((count(*)*100)/(select count(*) from cte 
where ranking = 1),2) as "immediate_percentage" from cte 
where ranking = 1 and 
order_date =customer_pref_delivery_date  ; 