select customer_id from 
(select customer_id, count(distinct product_key) as "total"
from customer
group by customer_id ) as t1 
where 
total = (select count(product_key) from product ) ; 