# Write your MySQL query statement below
with cte as
(select 
t2.name as "Department", t1.name as "Employee",
t1.salary as "Salary"
from employee as t1 
inner join 
department as t2 
on t1.departmentid = t2.id)

select Department, Employee, Salary from 
(select 
*, dense_rank() over (partition by Department order by Salary desc) as "ranking"
from cte) as t3 
where ranking <= 3 ;