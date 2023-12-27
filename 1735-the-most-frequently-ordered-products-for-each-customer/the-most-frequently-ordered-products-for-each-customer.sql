with cte as 
(select *, dense_rank() over (partition by customer_id order by total desc ) as "ranking"
from (select customer_id, product_id, count(product_id) as "total"
from orders 
group by customer_id, product_id ) as t1 )


select t2.customer_id, t2.product_id, t1.product_name from cte as t2 
inner join 
products as t1 
on t1.product_id = t2.product_id 
where ranking = 1 ;