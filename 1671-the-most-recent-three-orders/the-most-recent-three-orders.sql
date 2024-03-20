with cte as
(select 
t1.name as "customer_name",
t1.customer_id, 
t2.order_id, 
t2.order_date, 
dense_rank() over (partition by t1.customer_id order by t2.order_date desc) as "ranking"
 from 
customers as t1 
inner join 
orders as t2 
on t1.customer_id = t2.customer_id )

select customer_name,
customer_id, 
order_id, 
order_date 
from cte 
where ranking <= 3
order by customer_name asc, customer_id asc, order_date desc ;