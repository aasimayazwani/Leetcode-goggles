# Write your MySQL query statement below
select problem_id
    from        
    (select problem_id, likes/(likes+dislikes) as "ranking"
    from 
    problems) as t1 
    where ranking < 0.6 
    order by problem_id asc ; 