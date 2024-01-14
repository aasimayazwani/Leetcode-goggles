# Write your MySQL query statement below
# Pseudo Code
# keep track of the network between user1 and user2
# Remember its possible for user_id to be present in user2 list and not in the other way. 
# Otherwise just a union statement followed by group by statement

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