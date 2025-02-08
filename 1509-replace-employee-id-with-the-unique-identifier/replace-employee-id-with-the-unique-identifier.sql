# Write your MySQL query statement below
select 
ifnull(t2.unique_id,Null) as "unique_id", 
t1.name
from employees as t1 
left join 
employeeuni as t2 
on 
t1.id = t2.id ;