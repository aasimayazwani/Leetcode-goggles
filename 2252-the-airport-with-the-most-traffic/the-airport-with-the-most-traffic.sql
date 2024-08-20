# Write your MySQL query statement below

with cte as
(select airport_id, sum(flights_count) as "flights_count" from 
(select departure_airport as "airport_id", flights_count from flights 
union all 
select arrival_airport as "airport_id", flights_count from flights) as t1 
group by airport_id)


select airport_id from
(select *, dense_rank() over (order by flights_count desc)
 as "ranking" from cte ) as t3 
where ranking = 1