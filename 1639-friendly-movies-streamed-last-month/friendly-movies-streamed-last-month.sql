# Write your MySQL query statement below
with cte as
(select date_format(program_date,"%Y-%m") as "val", content_id 
from tvprogram)

select distinct title from cte as t1 
left join 
content as t2 
on 
t1.content_id = t2.content_id 
where 
t2.kids_content = "Y" and 
t2.content_type ="Movies" and 
t1.val ="2020-06"; 