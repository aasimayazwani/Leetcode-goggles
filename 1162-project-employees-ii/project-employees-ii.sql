# Write your MySQL query statement below
with cte as 
(select project_id, dense_rank() over (order by total desc ) as "ranking" from 
(select project_id, count(distinct employee_id) as "total" from project 
group by project_id) as t1 )

select project_id from cte 
where ranking = 1 ; 