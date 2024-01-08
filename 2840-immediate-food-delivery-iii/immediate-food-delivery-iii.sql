# Write your MySQL query statement below
with cte as (select *, 
case 
    when order_date = customer_pref_delivery_date then 1 
    else 0 
    end 
    as "counting", 
    count(delivery_id) over (partition by order_date) as "total"
from delivery)


select order_date, round(sum(counting)*100/avg(total),2) as "immediate_percentage"
from cte 
group by order_date