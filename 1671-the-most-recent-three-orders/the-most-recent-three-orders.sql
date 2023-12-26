with cte as 
(select *, dense_rank() over (partition by customer_id order by order_date desc ) as "ranking" 
from orders )


select t1.name as "customer_name",
t1.customer_id, 
t2.order_id, 
t2.order_date
 from cte as t2
inner join customers as t1 
on t1.customer_id = t2.customer_id 
where ranking <= 3
order by t1.name asc, t1.customer_id asc, t2.order_date desc  ; 