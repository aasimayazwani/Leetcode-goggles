# Write your MySQL query statement below
with cte as 
(select candidateid, dense_rank() over (order by total desc) as "ranking" from  
(select candidateid, count(id) as "total"
from vote 
group by candidateid ) as t1 
)

select distinct candidate.name from cte
inner join candidate 
on cte.candidateid = candidate.id
where cte.ranking = 1  ; 