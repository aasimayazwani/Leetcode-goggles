# Write your MySQL query statement below
with cte as
    (select 
    interview_id, sum(score) as "total"
    from rounds
    group by interview_id)

select candidate_id
    from
    (select  
    t1.candidate_id, t1.interview_id, t2.total, t1.years_of_exp
    from 
    candidates as t1 
    inner join cte as t2 
    on 
    t1.interview_id = t2.interview_id) as t3 
    where 
    years_of_exp >=2 and 
    total > 15 ; 