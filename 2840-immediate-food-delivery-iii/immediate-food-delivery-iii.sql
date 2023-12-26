# Write your MySQL query statement below
with cte as
(select order_date,customer_pref_delivery_date, count(delivery_id ) over (partition by order_date) as "total", 
case when order_date =  customer_pref_delivery_date then 1 
else 0 
end as "reward"
from delivery) 

select order_date, round(((sum(reward)*100)/total),2) as "immediate_percentage" from cte 
group by order_date
order by order_date asc ; 
