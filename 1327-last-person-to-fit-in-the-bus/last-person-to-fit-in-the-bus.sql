select person_name  from
(select person_name, Total_Weight  from 
(select 
*, 
sum(weight) over (order by turn asc) as "Total_Weight"
from queue) as t1 
where Total_Weight <= 1000 order by Total_Weight desc )  as t2 
limit 1 ;