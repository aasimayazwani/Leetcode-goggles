# Write your MySQL query statement below
select email
    from
    (select email, count(*) as "counting"
    from person
    group by email) as t1 
    where counting > 1 ; 