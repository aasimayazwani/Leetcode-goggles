# Write your MySQL query statement below
select t1.name as "warehouse_name", sum(t1.units*t2.width*t2.height*t2.length) as "volume" 
from Warehouse as t1 
inner join 
products as t2 
on 
t1.product_id = t2.product_id
group by t1.name ; 