with cte as
(select *, dense_rank() over (partition by player_id order by smallest asc) as "ranking"
from
(select player_id, device_id, min(event_date) as "smallest"
from activity
group by player_id, device_id) as t1 
)

select player_id, device_id from cte 
where ranking = 1 ; 