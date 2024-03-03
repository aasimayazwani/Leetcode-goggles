# Write your MySQL query statement below
with cte as 
(select airport_id, sum(flights_count) as "total"
from 
(select departure_airport as "airport_id", flights_count from flights
union all 
select arrival_airport as "airport_id", flights_count from flights) as r1 
group by airport_id) 

select airport_id from
(select *, dense_rank() over (order by total desc) as "ranking" from cte )
as t1 
where ranking = 1 ;