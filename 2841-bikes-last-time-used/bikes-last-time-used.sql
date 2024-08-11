# Write your MySQL query statement below
select bike_number, end_time from
(select bike_number, max(end_time) as "end_time"
from bikes
group by bike_number ) as t1 
order by end_time desc ; 