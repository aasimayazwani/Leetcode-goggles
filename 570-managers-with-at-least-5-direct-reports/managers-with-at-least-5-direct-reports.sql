# Write your MySQL query statement below
with cte as 
(select managerid, count(id) as "counting" 
from employee 
group by managerid 
having counting >= 5) 

select t2.name from cte as t1 
inner join employee as t2 
on t1.managerid = t2.id ; 