with cte as
(select *, dense_rank() over (partition by user_id order by visit_date asc) as "ranking"
from 
((select distinct user_id, "2021-1-1" as "visit_date"
from uservisits)
UNION ALL 
(select user_id, visit_date from uservisits)) as t1 )

select user_id, max(biggest_window) as "biggest_window"
from
(select t1.user_id, datediff(t2.visit_date,t1.visit_date) as "biggest_window" 
from cte as t1, cte as t2 
where 
t1.user_id = t2.user_id and 
t1.ranking < t2.ranking and t2.ranking - t1.ranking = 1 ) as t5 
group by user_id 
order by user_id ; 