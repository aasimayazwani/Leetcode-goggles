# Write your MySQL query statement below
select username, activity, startdate, enddate 
from
(select 
*, 
count(username) over (partition by username) as "total",
dense_rank() over (partition by username order by startdate desc) as "ranking"
from useractivity ) as t1 
where 
ranking = 2 or total = 1 ; 
