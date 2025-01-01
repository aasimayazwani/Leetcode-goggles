with cte as
    (select order_id, product_id, order_date
        from
        (select *, dense_rank() over (partition by product_id order by order_date desc)
        as "ranking"
        from orders) as t1 
        where ranking = 1 )

select 
t3.product_name, 
t3.product_id, 
t2.order_id, 
t2.order_date
from cte as t2 
inner join 
products as t3 
on 
t2.product_id = t3.product_id 
order by t3.product_name asc, 
t3.product_id asc, t2.order_id asc ; 