# Write your MySQL query statement below
with cte as
(select user_id, sum(distance) as "distance"
from rides 
group by user_id 
order by distance) 

select users.name, ifnull(cte.distance,0) as "travelled_distance" from users 
left join
cte 
on users.id = cte.user_id 
order by distance desc, users.name asc  ; 