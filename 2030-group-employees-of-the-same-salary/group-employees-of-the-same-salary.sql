# Write your MySQL query statement below
with cte as
    (select employee_id, name, salary from 
        (select *, 
        count(employee_id) over (partition by salary) as "counting"
        from employees) as t1 
    where counting > 1  ) 

select *, dense_rank() over (order by salary )as "team_id"
from cte 
order by team_id asc,employee_id asc  ;