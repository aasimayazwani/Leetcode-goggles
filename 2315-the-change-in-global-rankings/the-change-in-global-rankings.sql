# Write your MySQL query statement below
with cte as
(select t1.team_id,t1.name, t1.points, t1.points + t2.points_change as "new_points" from  teampoints as t1 
inner join pointschange as t2 
on t1.team_id = t2.team_id)

select distinct team_id, name, cast(ranking as signed) - cast(new_ranking as signed)  as "rank_diff" from 
(select *, dense_rank() over (order by points desc, name asc) as "ranking", 
          dense_rank() over (order by new_points desc, name asc) as "new_ranking"
          from cte) as t4 ; 