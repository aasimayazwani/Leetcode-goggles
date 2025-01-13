# Write your MySQL query statement below
with cte as
    (select managerid
        from
        (select managerid, count(id) as "counting"
        from employee
        group by managerid) as t1
        where counting >= 5)

select 
p2.name 
from cte as p1 
inner join 
employee as p2 
on 
p1.managerid = p2.id