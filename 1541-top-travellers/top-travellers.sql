with cte as 
(select user_id, sum(distance) as "travelled_distance"
from rides
group by user_id )


select t1.name, 
ifnull(t2.travelled_distance,0) as "travelled_distance" from users as t1 
left join cte as t2 
on t1.id = t2.user_id 
order by travelled_distance desc, name asc ; 