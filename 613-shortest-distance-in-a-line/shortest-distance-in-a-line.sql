# Write your MySQL query statement below
select min(abs(t1.x - t2.x)) as "shortest" from point as t1, point as t2 
where t1.x != t2.x ; 