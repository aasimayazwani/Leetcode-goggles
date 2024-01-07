with cte as
((select from_id as "person1", to_id as "person2", duration 
from calls)
UNION ALL
(select to_id as "person1", from_id as "person2", duration 
from calls))

select * from 
(select person1, person2, count(*) as "call_count",
sum(duration) as "total_duration" from cte
group by person1, person2) as t3 
where person1 < person2 ; 