# Write your MySQL query statement below
with cte as 
(select customer_id from 
(select distinct t1.customer_id from Orders as t1 , Orders as t2 
where t1.customer_id  = t2.customer_id and 
t1.product_name = "A" and t2.product_name = "B") as t3 
where customer_id not in (select distinct customer_id from orders where 
product_name ="C"))

select cte.customer_id, customers.customer_name from cte inner join customers 
on customers.customer_id = cte.customer_id
order by customer_id asc ;  