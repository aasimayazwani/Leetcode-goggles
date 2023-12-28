  # Write your MySQL query statement below
with cte as 
(  select passenger_id, count(ride_id) as "cnt"
  from rides 
  where passenger_id in (select distinct driver_id from rides) 
  group by passenger_id 
)

select t3.driver_id, ifnull(cnt,0) as "cnt" 
from (select distinct driver_id from rides) as t3  
left join cte
on  cte.passenger_id = t3.driver_id ; 