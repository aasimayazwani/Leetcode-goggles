# Write your MySQL query statement below
with cte as
    (select 
        row_number() over (order by first_col) as "ranking", first_col from data ),

cte2 as
    (select 
        row_number() over (order by second_col desc) as "ranking", second_col from data 
        order by ranking desc )

select p1.first_col, p2.second_col 
from 
cte as p1 
inner join 
cte2 as p2 
on 
p1.ranking = p2.ranking