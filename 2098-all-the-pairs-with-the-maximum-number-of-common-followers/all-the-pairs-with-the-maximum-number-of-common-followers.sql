# Write your MySQL query statement below
with cte as 
(select *, count(*) as "counting"
from
(select t1.user_id as "user1_id", t2.user_id as "user2_id", t1.follower_id  from relations as t1, 
relations as t2 
where 
t1.user_id != t2.user_id and 
t1.follower_id = t2.follower_id 
and  t1.user_id < t2.user_id)  as t3 
group by user1_id, user2_id )

select user1_id, user2_id from
(select *, dense_rank() over (order by counting desc) as "ranking"
from cte )
as t4 
where ranking = 1 ;

