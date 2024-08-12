# Write your MySQL query statement belowselect 
select class from 
(select class, count(distinct student) as "counting"
from courses 
group by class) as t1 
where counting >= 5 