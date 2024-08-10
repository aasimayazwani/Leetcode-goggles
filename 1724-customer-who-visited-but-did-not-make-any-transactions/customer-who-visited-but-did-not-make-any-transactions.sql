select customer_id, count(*) as "count_no_trans"
from
(select customer_id from visits 
where visit_id not in (select visit_id from transactions)) as t1 
group by customer_id ; 