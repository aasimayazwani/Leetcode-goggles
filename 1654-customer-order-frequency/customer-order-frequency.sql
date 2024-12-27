# Write your MySQL query statement belowse
with cte as
(select 
t2.customer_id, 
t1.price*t2.quantity as "total",
date_format(t2.order_date,"%Y-%m") as "date"
from product as t1 
inner join 
orders as t2 
on 
t1.product_id = t2.product_id),

cte2 as
(select customer_id, date,sum(total) as "total" 
from cte 
group by customer_id, date ), 

cte3 as
(select distinct p1.customer_id  from cte2 as p1, cte2 as p2 
where p1.customer_id = p2.customer_id and 
p1.date = "2020-06" and p2.date = "2020-07" and 
p1.total >= 100 and p2.total >= 100)

select r1.customer_id, r1.name  from customers as r1
inner join 
cte3 as r2 
on 
r1.customer_id = r2.customer_id 