# Write your MySQL query statement below
with cte as
    (select user_id, sum(distance) as "traveled_distance"
    from rides
    group by user_id)

select 
t1.user_id, t1.name as "name",ifnull(t2.traveled_distance,0) as "traveled distance"
from users as t1 
left join 
cte as t2 on 
t1.user_id = t2.user_id 
order by user_id asc ; 