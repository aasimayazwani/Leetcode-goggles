select t2.product_name, t1.unit from
(select product_id, sum(unit) as "unit"
from orders
where date_format(order_date,"%m-%Y") = "02-2020"
group by product_id
) as t1 
inner join 
products as t2 
on t1.product_id = t2.product_id 
where unit >= 100 ; 
