# Write your MySQL query statement below

with cte as
(select city, peak_hour,count(*) as 'total' from
(select *, hour(call_time) as "peak_hour"
from calls) as t1 
group by city, peak_hour)

select city, peak_hour as "peak_calling_hour",
total as number_of_calls from 
(select *, dense_rank() over (partition by city order by total desc) as "ranking"
from cte ) as t2 
where ranking = 1 
order by peak_calling_hour desc, city desc ;