select name, travelled_distance from
(select 
t1.id,
t1.name, ifnull(sum(ifnull(t2.distance,0)),0) as "travelled_distance"
from users as t1 
left join 
rides as t2 
on 
t1.id = t2.user_id 
group by t1.id ) as t3 
order by travelled_distance desc, name asc ; 