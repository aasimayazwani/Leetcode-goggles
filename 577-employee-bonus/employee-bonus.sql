# Write your MySQL query statement below
select 
t1.name, ifnull(t2.bonus,null) as "bonus" 
from employee as t1 
left join 
bonus as t2 
on 
t1.empid = t2.empid 
where bonus is null or bonus < 1000; 