select id from 
(select *, 
lag(recorddate) over (order by recorddate) as "previous_date",
lag(temperature) over (order by recorddate) as "previous"
from weather) as t1 
where previous < temperature and datediff(recorddate,previous_date) = 1; 