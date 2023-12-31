# Write your MySQL query statement belows
with cte as (select product_id, sum(unit) as "total" from 
(select *, date_format(order_date,"%Y-%m") as "date"
from orders) as t1 
where date = "2020-02" 
group by product_id )


select t2.product_name, t3.total as "unit"  from products as t2 
inner join cte as t3 
on t2.product_id = t3.product_id 
having unit >= 100 ; 