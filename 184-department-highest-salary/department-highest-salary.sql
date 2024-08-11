with cte as 
(select name, salary, departmentid, ranking from
(select *, dense_rank() over (partition by departmentid order by salary desc) as "ranking"
from employee) as t1 
)

select t2.name as "Department",
t1.name as "Employee", t1.salary as "Salary" from cte as t1 inner join 
department as t2
on t1.departmentid = t2.id 
where t1.ranking = 1 ; 