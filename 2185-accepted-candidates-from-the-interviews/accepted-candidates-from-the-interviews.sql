select candidate_id from
(select t1.candidate_id, sum(t2.score)  as "total" 
from 
(select candidate_id, interview_id from candidates 
where years_of_exp >= 2 ) as t1 
inner join 
rounds as t2 
on t1.interview_id = t2.interview_id
group by t1.candidate_id) as t3 
where 
total > 15 ; 