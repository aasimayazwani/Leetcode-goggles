with cte as 
(select order_date, order_id, product_id from 
(select *, dense_rank() over (partition  by product_id order by order_date desc) 
as "ranking"
from orders) as t5 
where ranking = 1 )


select t2.product_name, t2.product_id, t1.order_id, t1.order_date from cte as t1
inner join products as t2 
on t1.product_id = t2.product_id
order by product_name asc, product_id asc, order_id asc  ; 