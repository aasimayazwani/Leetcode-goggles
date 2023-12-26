# Write your MySQL query statement below
with cte as
(select sqrt((t1.x - t2.x)*(t1.x - t2.x) + 
            (t1.y-t2.y)*(t1.y-t2.y)) as "shortest" 
from point2d as t1, point2d as t2 
having shortest != 0)

select round(min(shortest),2) as "shortest" from cte ; 