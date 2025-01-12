# Write your MySQL query statement below
with cte as
    (select 
    t1.name, count(t2.candidateid) as "counting"
    from candidate as t1 
    inner join 
    vote as t2 
    on 
    t1.id = t2.candidateid 
    group by t1.name)

select name
    from
    (select *, dense_rank() over (order by counting desc) as "ranking"
    from cte) as t3 
    where ranking = 1 ; 