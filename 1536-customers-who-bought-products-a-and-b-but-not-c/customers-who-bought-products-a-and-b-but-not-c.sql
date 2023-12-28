# Write your MySQL query statement below
with cte as 
(select t1.customer_id from orders as t1 
inner join orders as t2 
on t1.customer_id = t2.customer_id 
where t1.product_name ="A" and 
t2.product_name = "B" 
and t1.customer_id not in (select customer_id from orders 
where product_name = "C") )


select distinct t3.customer_id, t3.customer_name from customers as t3
inner join cte as t4 
on t4.customer_id = t3.customer_id 
order by t3.customer_id asc ; 