with cte as 
(select product_id, order_id, order_date from
(select *, dense_rank() over (partition by product_id order by order_date desc) as "ranking" 
from orders) as t1
where ranking = 1)


select  
t2.product_name, t2.product_id, cte.order_id, cte.order_date
from cte
inner join 
products as t2 
on t2.product_id = cte.product_id 
order by product_name asc, product_id asc, order_id asc
 ;