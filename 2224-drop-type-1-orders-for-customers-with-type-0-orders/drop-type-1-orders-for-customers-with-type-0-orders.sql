select * from orders 
where 
order_id not in (select t1.order_id from orders as t1 , orders as t2 
where 
t1.customer_id = t2.customer_id and 
t1.order_type = 1 and 
t2.order_type = 0) ; 