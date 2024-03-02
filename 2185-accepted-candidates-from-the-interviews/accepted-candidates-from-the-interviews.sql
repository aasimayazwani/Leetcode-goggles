# Write your MySQL query statement below
with cte as
(select candidate_id, years_of_exp, 
sum(score) over (partition by candidate_id) as "total"
from candidates as t1 
inner join 
rounds as t2 
on t1.interview_id = t2.interview_id) 

select distinct candidate_id from cte 
where years_of_exp >=2 and 
total > 15 