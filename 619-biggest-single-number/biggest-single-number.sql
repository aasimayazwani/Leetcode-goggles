# Write your MySQL query statement below
select ifnull(max(num),null) as "num" from
(select *, count(num) as "counting"
from mynumbers 
group by num ) as t1 
where counting = 1 