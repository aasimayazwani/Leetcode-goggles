# Write your MySQL query statement below
with cte as
    (select from_id as "person1", to_id  as "person2", duration from calls
    union all 
    select to_id  as "person1", from_id  as "person2", duration from calls)

select person1, person2, count(*) as "call_count" , 
sum(duration) as "total_duration"
from cte
where person1 < person2
group by person1, person2