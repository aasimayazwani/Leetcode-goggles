with cte as 
(select *, dense_rank() over (order by counting asc ) as "lowest",
dense_rank() over (order by counting DESC ) as "highest"
from 
(select activity, count(activity) as "counting"
from friends 
group by activity
) as t1 )


select distinct  activity from cte 
where activity not in 
(select distinct activity from cte 
where lowest = 1
UNION ALL 
select distinct activity from cte 
where highest = 1 )