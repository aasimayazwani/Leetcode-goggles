with cte as
(select first_col, row_number() over () as "counting" from
(select first_col 
from data 
order by first_col asc)  as t1)

select first_col,second_col from cte 
inner join 
(select second_col, row_number() over () as "counting" from
(select second_col 
from data 
order by second_col desc)  as t2) as t3 
on cte.counting = t3.counting ;