# Write your MySQL query statement below
select ifnull(max(num),null) as "num"
    from
    (select num, count(*) as "counting"
    from mynumbers 
    group by num) as t1 
    where counting = 1