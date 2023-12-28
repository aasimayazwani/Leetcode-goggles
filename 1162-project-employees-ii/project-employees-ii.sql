# Write your MySQL query statement below
with cte as 
(select distinct project_id, cnt from (select *, count(employee_id) over (partition by project_id) as "cnt" 
from project ) as t1 )

select project_id from
(select *, dense_rank() over (order by cnt desc ) as "ranking" 
from cte) as t2 
where ranking = 1 ; 