select person_name from 
(select *, sum(weight) over (order by turn) as "Total_Weight"
from queue ) as t1  
where Total_Weight <= 1000
order by Total_Weight desc limit 1 ;