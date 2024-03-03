# Write your MySQL query statement below
with cte as 
(select *, dense_rank() over (order by points1 desc, name asc ) as "ranking1",
          dense_rank() over (order by points2 desc, name asc) as "ranking2"
from 
(select t1.team_id, t1.name, 
t1.points as "points1", 
t1.points + t2.points_change as "points2"
from teampoints as t1 
inner join 
pointschange as t2 
on t1.team_id = t2.team_id) as t1 )

select team_id, name, cast(ranking1 as signed) - cast(ranking2 as signed) as "rank_diff" from 
cte ; 