# Write your MySQL query statement below
with cte as (select first_col, ROW_NUMBER() OVER(ORDER BY first_col ASC) as "ranking1" from data) 

select t1.first_col, t2.second_col  from cte as t1 
inner join
(select second_col, ROW_NUMBER() OVER(ORDER BY second_col desc ) as "ranking2" from data ) as t2 
on t1.ranking1 = t2.ranking2