# Write your MySQL query statement below
with cte as
    (select name, departmentid, salary
        from
        (select *, dense_rank() over (partition by departmentid order by salary desc)
            as "ranking"
            from employee) as t1 
        where 
        ranking = 1)

select
p2.name as "Department",
p1.name as "Employee",
p1.salary as "Salary"
from 
cte as p1 
inner join 
department as p2 
on 
p1.departmentid = p2.id ; 