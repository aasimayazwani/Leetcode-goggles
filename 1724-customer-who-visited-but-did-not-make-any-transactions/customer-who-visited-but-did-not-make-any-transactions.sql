with cte as
    (select visit_id, customer_id
    from visits
    where 
    visit_id not in 
    (select visit_id from transactions) ) 

select customer_id, count(visit_id) as "count_no_trans"
from 
cte 
group by customer_id ; 