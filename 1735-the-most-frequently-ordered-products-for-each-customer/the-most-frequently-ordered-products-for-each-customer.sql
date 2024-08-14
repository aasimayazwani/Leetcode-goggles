# Write your MySQL query statement below
with cte as 
(select customer_id, 
        product_id, 
        dense_rank() over (partition by customer_id order by total desc) as "ranking"
        from
        (select customer_id, product_id, count(*) as "total"
        from orders
        group by customer_id, product_id) as t1 )

select 
t2.customer_id, 
t2.product_id, 
t3.product_name
from cte as t2 
inner join 
products as t3 
on t2.product_id = t3.product_id 
where t2.ranking = 1 