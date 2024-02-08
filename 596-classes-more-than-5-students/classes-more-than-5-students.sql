# Write your MySQL query statement belowselect 
select class from 
(select class, count(distinct student) as "total"
from courses
group by class
having total >= 5) as t1 