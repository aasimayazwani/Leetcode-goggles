# Write your MySQL query statement below
with cte as 
(select dep_id, count(distinct emp_id) as 'counting'
from employees
group by dep_id)

select employees.emp_name as "manager_name", employees.dep_id from employees 
inner join 
(select dep_id from 
(select *, dense_rank() over (order by counting desc ) as "ranking"
from cte )
as t3 
where ranking = 1 ) as t5 
on t5.dep_id = employees.dep_id
where  employees.position = "Manager"
order by dep_id asc ;