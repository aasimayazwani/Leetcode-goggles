# Write your MySQL query statement below
with cte as 
(select  
sum(t1.price*t2.quantity) as "total",
t2.customer_id , 
date_format(t2.order_date,"%Y-%m") as "time" 
from product as t1 
inner join orders as t2 
on t1.product_id = t2.product_id 
group by t2.customer_id, time )

select df1.customer_id, df1.name  from customers as df1 
inner join 
(select distinct t1.customer_id from cte as t1, cte as t2 
where t1.customer_id = t2.customer_id 
and 
t1.time = "2020-06" and t2.time = "2020-07"  and 
t1.total >= 100 and t2.total >= 100 ) as df2 
on df1.customer_id = df2.customer_id ; 