# Write your MySQL query statement below
with cte as
(select 
t1.product_name, 
t2.buyer_id 
from 
product as t1
inner join 
sales as t2 
on 
t1.product_id = t2.product_id)

select distinct buyer_id from cte 
where product_name = "S8" and 
buyer_id not in (select buyer_id from cte where product_name = "iPhone") ; 
