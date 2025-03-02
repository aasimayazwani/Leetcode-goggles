# Write your MySQL query statement below
select distinct problem_id
    from
    (select problem_id, ((likes)/(likes+dislikes)) as "percent"
    from problems) as t1 
    where percent < 0.6 
    order by problem_id asc ; 