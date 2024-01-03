# Write your MySQL query statement below
with cte as 
(select t1.candidate_id,t1.years_of_exp,t1.interview_id,
        t2.round_id,t2.score
 from candidates as t1 
inner join 
rounds as t2 
on t1.interview_id = t2.interview_id) 

select distinct candidate_id from 
(select *, sum(score) over (partition by candidate_id) as "total"
from cte ) as t3 
where total > 15 and 
years_of_exp >= 2 ; 