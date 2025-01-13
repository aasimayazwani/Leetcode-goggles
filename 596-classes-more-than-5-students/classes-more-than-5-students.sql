# Write your MySQL query statement below
select distinct class
    from
    (select class, count(*) as "counting"
    from courses
    group by class) as t1 
    where counting >= 5 ; 