with cte as
(select order_id, order_date, customer_id from
(select *, dense_rank() over (partition by customer_id order by order_date desc) as "ranking"
from orders) as e1
where ranking <= 3)


select t1.name as "customer_name",
t2.customer_id, 
t2.order_id, 
t2.order_date 
 from cte as t2 
inner join 
customers as t1 
on t2.customer_id = t1.customer_id 
order by customer_name asc, customer_id asc, order_date desc ;