# Write your MySQL query statement below
select 
t1.id, t1.year, ifnull(t2.npv,0) as "npv"
from queries as t1 
left join 
npv as t2 
on
t1.id = t2.id and t1.year = t2.year ; 