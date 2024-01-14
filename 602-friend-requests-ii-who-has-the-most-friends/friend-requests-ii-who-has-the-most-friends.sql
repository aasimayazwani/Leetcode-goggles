# Write your MySQL query statement below
with cte as
(select person1, count(distinct person2) as "counting"
from
((select requester_id as "person1", 
        accepter_id as "person2"
        from RequestAccepted )
UNION ALL 
(select 
accepter_id as "person1",
requester_id as "person2" 
        from RequestAccepted ))
as t4 
group by person1 )

select person1 as "id", counting as "num"
from
(select *, dense_rank() over (order by counting desc) as "ranking"
from cte) as t5
where ranking = 1 