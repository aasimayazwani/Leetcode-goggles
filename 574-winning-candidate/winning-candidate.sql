# Write your MySQL query statement below
with cte as 
(select *, dense_rank() over (order by counting desc) as "ranking"
from
(select candidateid, count(candidateid) as "counting"
from vote 
group by candidateid) as t1 )


select candidate.name from candidate 
inner join 
(select * from cte where ranking = 1 ) as t2 
on candidate.id = t2.candidateId ; 