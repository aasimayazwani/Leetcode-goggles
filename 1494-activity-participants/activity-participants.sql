# Write your MySQL query statement below
with cte as
(select activity,count(name) as "total" 
from friends
group by activity)


select distinct activity from cte 
where total not in (
    select min(total) from  cte 
    UNION ALL
    select max(total) from  cte 
)