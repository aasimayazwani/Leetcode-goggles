select distinct actor_id, director_id from 
(select actor_id, director_id, count(timestamp) as "total"
from actordirector
group by actor_id, director_id 
having total >= 3 ) as t4 ; 