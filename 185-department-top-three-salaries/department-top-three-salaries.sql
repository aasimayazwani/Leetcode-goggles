# Write your MySQL query statement below
select t2.name as "Department", 
t1. name as "Employee",
t1.salary as "Salary" from 
(select *, dense_rank() over (partition by departmentId order by salary desc ) as "ranking"
from Employee ) as t1 
inner join department as t2 
on t1.departmentId = t2.id 
where ranking <= 3 ; 