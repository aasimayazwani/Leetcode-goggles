# Write your MySQL query statement below
with cte as 
(select 
t2.name as "Department",
t1.name as "Employee",
t1.salary as "Salary",
dense_rank() over (partition by t2.name order by t1.salary desc ) as "Ranking"
from Employee as t1 
inner join Department as t2  on
t1.departmentId = t2.id )

select Department, Employee, Salary 
from cte 
where Ranking = 1 ; 