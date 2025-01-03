# Write your MySQL query statement belowse
with cte as
(select 
t2.customer_id, 
date_format(order_date,"%Y-%m") as "mon_val",
t1.price*t2.quantity as "total"
from product as t1 
inner join
orders as t2 
on 
t1.product_id = t2.product_id 
),
cte2 as
(select customer_id, mon_val, sum(total)  as "total"
from cte
group by customer_id, mon_val),

cte3 as
(select p1.customer_id from cte2 as p1, cte2 as p2 
where 
p1.customer_id = p2.customer_id and 
p1.mon_val = "2020-06" and 
p2.mon_val = "2020-07" and
p1.total >= 100 and 
p2.total >= 100)

select q1.customer_id, q2.name from 
cte3 as q1 
inner join 
customers as q2 
on 
q1.customer_id = q2.customer_id 