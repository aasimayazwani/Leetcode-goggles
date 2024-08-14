with cte as 
(select t1.team_id, t1.name,
        t1.points,
        t1.points + t2.points_change as "new_points"
        from teampoints as t1 
        inner join PointsChange t2 
        on t1.team_id = t2.team_id 
)

select team_id, name, cast(ranking1 as signed) - cast(ranking2 as signed) as "rank_diff"
from
(select team_id, name, 
        dense_rank() over (order by points desc, name asc) as "ranking1",
        dense_rank() over (order by new_points desc, name asc) as "ranking2"
        from 
        cte) as t3 
    