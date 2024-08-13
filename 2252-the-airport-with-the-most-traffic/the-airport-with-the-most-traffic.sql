with cte as 
(select airport_id, sum(flights_count) as "counting" from
((select departure_airport as "airport_id", flights_count from flights)
UNION ALL
(select arrival_airport as "airport_id", flights_count from flights)) as t1 
group by airport_id)

select airport_id from
(select *, dense_rank() over (order by counting desc) as 'ranking'
from cte  ) as t4 
where ranking = 1 ; 