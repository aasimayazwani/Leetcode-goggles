with cte as 
(select passenger_id, count(ride_id) as "cnt"
from rides 
group by passenger_id )

select t1.driver_id, ifnull(t2.cnt,0) as "cnt" from 
(select distinct driver_id from rides) as t1 
left join
cte as t2
on  t1.driver_id = t2.passenger_id ; 

