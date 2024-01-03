with cte as
(select customer_id, order_id, order_date, 
dense_rank() over (partition by customer_id order by order_date desc ) as "ranking"
from orders )

select t1.name as "customer_name",
t2.customer_id, t2.order_id, t2.order_date
 from 
customers as t1 
inner join 
cte as t2 
on t1.customer_id  = t2.customer_id 
where ranking <= 3 
order by customer_name asc, customer_id asc, order_date desc; 