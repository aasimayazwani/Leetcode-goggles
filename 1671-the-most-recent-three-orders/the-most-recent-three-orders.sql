with cte as 
(select customer_id, order_id, order_date from 
(select *, dense_rank() over (partition by customer_id order by order_date desc) 
as "ranking" from orders ) as t1 
where ranking <= 3 )

select t2.name as "customer_name",
t3.customer_id, t3.order_id, t3.order_date from customers as t2 
inner join 
cte as t3 
on t2.customer_id = t3.customer_id 
order by customer_name asc, customer_id asc, order_date desc