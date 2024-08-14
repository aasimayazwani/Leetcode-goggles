with cte as
(select *, dense_rank() over (partition by gender order by user_id asc) as "ranking"
from genders)

select  user_id, gender from 
(select *, 1 as "position" from cte where gender  = "female" UNION ALL
select *, 3 as "position" from cte where gender  = "male" UNION ALL
select *, 2 as "position" from cte where gender  = "other") as t1 
order by ranking asc, position asc ; 