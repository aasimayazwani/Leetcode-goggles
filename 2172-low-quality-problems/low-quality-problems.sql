# Write your MySQL query statement below
with cte as 
(select distinct problem_id from
(select problem_id, likes, likes + dislikes as "total"
from problems) as t1 
where likes/total < 0.6 )

select problem_id from cte 
order by problem_id asc ; 