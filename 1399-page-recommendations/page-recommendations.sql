with cte as (select user, friend from
(select user1_id as "user", user2_id as "friend" 
from friendship
UNION ALL
select user2_id as "user", user1_id as "friend" 
from friendship) as df1
)

select distinct t2.page_id as "recommended_page" from cte as t1
inner join likes as t2 
on t1.friend = t2.user_id 
where t1.user = 1 and 
t2.page_id not in (select page_id from likes 
where user_id = 1 )