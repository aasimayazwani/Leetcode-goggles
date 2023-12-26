# Write your MySQL query statement below
select person_name from
(select *, sum(weight) over (order by turn) as "new_weight"
from queue)  as t1 
where new_weight <= 1000 
order by new_weight desc limit 1 ; 