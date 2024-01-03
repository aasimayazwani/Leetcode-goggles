# Write your MySQL query statement below
select * from orders where order_id not in (
select t2.order_id from orders as t1, orders as t2 
where t1.order_id != t2.order_id and 
t1.customer_id = t2.customer_id and 
t1.order_type = 0 and 
t2.order_type = 1) ; 