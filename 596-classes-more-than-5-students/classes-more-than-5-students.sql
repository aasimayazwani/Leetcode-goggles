# Write your MySQL query statement belowselect 
select class from 
(select class, count(class) as "total"
from courses 
group by class ) as t1 
where total >=5 ; 
