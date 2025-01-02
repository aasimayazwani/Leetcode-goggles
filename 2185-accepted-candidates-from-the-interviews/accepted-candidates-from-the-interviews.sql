with cte as
    (select  
    t1.candidate_id, t1.years_of_exp, t1.interview_id, t2.score
    from candidates as t1 
    inner join 
    rounds as t2 
    on 
    t1.interview_id = t2.interview_id )

select candidate_id
from
    (select candidate_id, sum(score) as "total", years_of_exp
    from cte 
    group by candidate_id) as t4 
where years_of_exp >= 2 and total > 15 ; 