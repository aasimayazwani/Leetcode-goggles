with cte as 
(select person_name from 
(select *, sum(weight) over (order by turn asc) as "total_weight"
from queue) as t1 
where total_weight <= 1000 
order by total_weight desc ) 

select person_name from cte limit 1 ; 