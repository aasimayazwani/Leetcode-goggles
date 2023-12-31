with cte as 
(select *, dense_rank() over (partition by player_id order by event_date asc ) 
as "ranking"
from activity ) 

select player_id, device_id from cte
where ranking = 1 