# Write your MySQL query statement belo
select actor_id, director_id from 
(select *, count(*)  as "counting"
from ActorDirector
group by actor_id, director_id ) as t1
where counting >= 3 ; 