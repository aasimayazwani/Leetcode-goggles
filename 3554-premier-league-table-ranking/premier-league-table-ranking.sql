# Write your MySQL query statement below
with cte as
(select 
team_id, 
team_name, 
3*wins + draws as "points"
from TeamStats )

select *, rank() over (order by points desc) as "position"
from cte
order by points desc, team_name asc ; 