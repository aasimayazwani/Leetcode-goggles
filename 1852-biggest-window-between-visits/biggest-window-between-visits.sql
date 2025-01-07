with cte as 
    ((select distinct user_id, "2021-1-1" as "visit_date"
    from UserVisits)
    union all 
    (select user_id, visit_date from uservisits)
    ),

cte2 as
(select *, row_number() over (partition by user_id order by visit_date asc ) as "ranking"
from cte )

select user_id, max(biggest_window) as "biggest_window"
    from
    (select p1.user_id, datediff(p2.visit_date,p1.visit_date) as "biggest_window"
    from cte2 as p1, cte2 as p2 
    where
    p1.user_id = p2.user_id and 
    cast(p2.ranking as signed) - cast(p1.ranking as signed) = 1) as p3 
    group by user_id 
    order by user_id asc ; 