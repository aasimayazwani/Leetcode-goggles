# Write your MySQL query statement below
select month, count(distinct order_id) as "order_count", count(distinct customer_id) as "customer_count"
from
(select date_format(order_date,"%Y-%m") as "month",  customer_id, order_date, order_id 
    from orders
    where invoice > 20)  as t1 
group by month; 