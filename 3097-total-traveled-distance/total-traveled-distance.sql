with cte as
(select user_id, sum(distance) as "travelled_distance"
from rides 
group by user_id) 

select distinct t1.user_id , t1.name ,ifnull(t2.travelled_distance,0) as 'traveled distance' from users as t1 
left join 
cte as t2 
on t1.user_id = t2.user_id
order by t1.user_id asc  ; 