# Write your MySQL query statement beloww
with cte as
(select voter, candidate, counting, sum(counting) over (partition by voter) as "total_votes"
    from
    (select *, 1 as counting from votes)
    as t1 ),

t4 as
    (select candidate, sum(real_votes) as "total"
    from
        (select voter, candidate, counting/total_votes as "real_votes" from cte 
        where candidate is not null ) as t2
        group by candidate 
    )

select candidate from
    (select *, dense_rank() over (order by total desc) as "ranking" from t4)
    as t5 
    where ranking = 1 
    order by candidate asc ;