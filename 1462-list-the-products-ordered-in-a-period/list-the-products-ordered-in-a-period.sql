# Write your MySQL query statement belows
select product_name, unit
from
(select t1.product_name, sum(t2.unit) as "unit" from products as t1 
inner join 
orders as t2 
on t1.product_id = t2.product_id 
where date_format(order_date,"%Y-%m") = "2020-02" 
group by t1.product_name) as t3 
where unit >= 100;