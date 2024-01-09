# Write your MySQL query statement below
with cte as 
(select airport, sum(flights_count) as "total_flights"
from
(select departure_airport as "airport", flights_count from flights 
UNION ALL 
select arrival_airport as "airport", flights_count from flights )
as t1 
group by airport) 

select airport as "airport_id" from
(select *, dense_rank() over (order by total_flights desc ) as "ranking"
from cte ) as t2 
where ranking = 1 ;