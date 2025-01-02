with c1 as
(select *, 
dense_rank() over (partition by customer_id order by order_date desc) as "ranking"
from orders
)

select 
c0.name as "customer_name", 
c1.customer_id, 
c1.order_id, 
c1.order_date 
from customers as c0 
inner join 
c1 
on 
c0.customer_id = c1.customer_id 
where ranking <= 3 
order by customer_name asc, customer_id asc, order_date desc ; 