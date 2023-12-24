# Write your MySQL query statement below
with cte as 
(select product_id, 
Width*Length*Height as "current"
from Products) 

select t2.name as "warehouse_name",
sum(t2.units*t1.current) as "volume"
 from cte as t1 inner join 
warehouse as t2
on t1.product_id = t2.product_id 
group by t2.name ; 