# Write your MySQL query statement below
with cte as 
(select person, count(distinct friend) as "total"
from 
    ((select user1 as "person",
    user2 as "friend"
    from friends)
    UNION ALL 
    (select user2 as "person",
    user1 as "friend"
    from friends)) as t1 
group by person)


select 
person as "user1", 
round((total/(select count(distinct person) from cte))*100,2) as "percentage_popularity"
from 
cte 
order by user1 asc ; 