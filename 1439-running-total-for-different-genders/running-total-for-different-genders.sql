select gender, day, total from
((select *, sum(score_points) over (partition by gender order by day) as "total"
from
(select gender, day, score_points 
from scores 
order by gender asc, day asc) as t1)) as t2 
order by gender, day   ;