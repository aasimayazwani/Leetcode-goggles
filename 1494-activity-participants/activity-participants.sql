# Write your MySQL query statement below
with cte as 
(select *, dense_rank() over (order by total asc) as "forward",
        dense_rank() over (order by total desc) as "backward" from 
(select activity, count(name) as "total"
from friends 
group by activity) as t1 )

select distinct activity from friends where activity not in 
(select activity from cte where forward = 1 or backward = 1)  ; 