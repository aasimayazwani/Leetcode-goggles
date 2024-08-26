select 
t1.user_id, t1.name, ifnull(sum(t2.distance),0) as "traveled distance"
 from users as t1 
left join 
rides as t2 
on t1.user_id = t2.user_id 
group by t1.user_id 
order by user_id asc ; 