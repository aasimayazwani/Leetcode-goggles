# Write your MySQL query statement below
select candidate_id from
(select 
t1.candidate_id,
avg(t1.years_of_exp) as "experience",
sum(t2.score) as "total_score"
from candidates as t1 
inner join rounds as t2 
on t1.interview_id = t2.interview_id
group by t1.candidate_id 
having total_score > 15 and experience >= 2) as t4   ; 