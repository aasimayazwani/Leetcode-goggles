with cte as 
(select project_id, employee_id, experience_years from
(select t1.project_id, t1.employee_id, t2.experience_years from project as t1 
inner join employee as t2 
on t1.employee_id = t2.employee_id ) as t1 )

select project_id, employee_id from 
(select *, dense_rank() over (partition by project_id order by experience_years desc) as "ranking"
from cte ) as t5 
where ranking = 1 