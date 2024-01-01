with cte as 
(select * from 
(select *, dense_rank() over (partition by departmentid order by salary desc)
as "ranking"
from employee ) as t1 
where ranking = 1)


select t3.name as "Department",
        t2.name as "Employee",
        t2.salary as "Salary"
 from cte as t2 inner join 
department as t3 
on t2.departmentid = t3.id ; 