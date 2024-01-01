# Write your MySQL query statement below
select gender, day, total from 
(select *, sum(score_points) over (partition by gender order by day asc) as "total"
from scores)  as t1 
order by gender asc, day asc ; 