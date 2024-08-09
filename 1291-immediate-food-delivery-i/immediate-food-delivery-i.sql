with cte as 
(select 
case
    when order_date != customer_pref_delivery_date then  0 
    when order_date = customer_pref_delivery_date then 1
end 
as  "total"
from delivery)


select round((sum(total)/count(total))*100,2) as "immediate_percentage"
from cte 