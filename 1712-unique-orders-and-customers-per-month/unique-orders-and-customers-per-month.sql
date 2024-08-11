select month, 
count(order_id) as "order_count", 
count(distinct customer_id) as "customer_count"
from 
(select order_id, customer_id, date_format(order_date,"%Y-%m") as 'month',
invoice 
from orders 
where invoice > 20 ) as t1 
group by month 