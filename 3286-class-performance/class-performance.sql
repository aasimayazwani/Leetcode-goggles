# Write your MySQL query statement below

with cte as
(select *, dense_rank() over (order by total desc) as "highest"
        , dense_rank() over (order by total asc) as "lowest"
from
(select student_id, assignment1 + assignment2 + assignment3
as "total"
from scores) as t3)


select distinct difference_in_score from 
(select total - (select total from cte where lowest = 1) as "difference_in_score"
from cte where highest = 1 ) as t6 ;