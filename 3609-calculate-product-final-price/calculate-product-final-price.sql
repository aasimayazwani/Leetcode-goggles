# Write your MySQL query statement below
select 
t1.product_id, 
t1.price*(1-(ifnull(t2.discount,0)/100)) as "final_price",
t1.category
from 
products as t1 
left join 
discounts as t2 
on 
t1.category  = t2.category 
order by t1.product_id asc ; 