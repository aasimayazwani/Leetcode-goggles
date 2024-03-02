select customer_id from 
(select customer_id, count(distinct product_key) as "counting"
from customer
group by customer_id
having counting = (select count(distinct product_key) from product)) 
as t1 ; 