select customer_number from 
(select customer_number, count(order_number) over (partition by customer_number) as "total" 
from orders 
order by total desc limit 1) as t1 