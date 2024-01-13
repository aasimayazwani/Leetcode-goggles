# Write your MySQL query statement below
with cte as
(select *, row_number() over () as "numbering"
from point2d)

select round(min(shortest),2) as "shortest" from 
(select sqrt((t1.x - t2.x)*(t1.x - t2.x) +
        (t1.y - t2.y)*(t1.y - t2.y)) as "shortest"
 from cte as t1, cte as t2 
where t1.numbering != t2.numbering) as t4 