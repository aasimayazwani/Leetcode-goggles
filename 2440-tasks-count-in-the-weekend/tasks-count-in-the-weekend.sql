with cte as 
(select task_id, date_format(submit_date,"%W") as "day_name" 
from tasks) 

select sum(day_value) as "weekend_cnt",
(select count(*) from tasks) - sum(day_value) as "working_cnt"
 from 
(select task_id, 
case 
    when day_name IN ("Saturday","Sunday") then 1 
    else 0 
    end 
as "day_value"
from cte ) as t1 