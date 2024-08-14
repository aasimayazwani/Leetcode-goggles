with cte as 
(select distinct product_id, order_id, order_date
from
(select product_id, order_id, order_date, 
    dense_rank() over (partition by product_id order by order_date desc) as "ranking"
    from orders) as t1 
    where ranking = 1)

select t2.product_name, 
        t1.product_id, 
        t1.order_id,
        t1.order_date 
 from cte as t1 
inner join 
products as t2 
on t1.product_id = t2.product_id 
order by product_name asc, product_id asc, order_id asc ; 