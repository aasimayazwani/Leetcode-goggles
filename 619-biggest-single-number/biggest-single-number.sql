# Write your MySQL query statement below
select ifnull(max(num),null) as "num"
from
(select num, 
count(num) over (partition by num) as "counting"
from mynumbers) as t1 
where counting = 1 ; 