with cte as 
(select 
t2.product_name,
t1.product_id, 
t1.order_id, 
t1.order_date, 
dense_rank() over (partition by t1.product_id order by order_date desc) as "ranking"
from orders as t1 
inner join 
products as t2 
on 
t1.product_id = t2.product_id )

select product_name, product_id, order_id, order_date
from cte 
where ranking = 1 
order by product_name asc, product_id asc,  order_id asc 
