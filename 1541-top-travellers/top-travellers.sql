# Write your MySQL query statement below
with cte as 
(select user_id, sum(distance) as "travelled_distance"
from rides
group by user_id)

select t2.name, ifnull(cte.travelled_distance,0) as "travelled_distance"  from users as t2 left join 
cte on 
cte.user_id = t2.id 
order by travelled_distance desc, name asc ; 