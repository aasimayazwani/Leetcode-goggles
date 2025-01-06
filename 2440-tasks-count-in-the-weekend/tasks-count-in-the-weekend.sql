with cte as
    (select 
        case 
            when day = 0 or day = 6 then "weekend"
            else 'weekday'
        end as "week"
        from
        (select date_format(submit_date,"%w") as 'day'
        from tasks) as t1),

cte2 as
(select *, count(*) "count" from cte 
group by week)

select 
p2.count as "weekend_cnt", p1.count as "working_cnt"
from cte2 as p1, cte2 as p2 
where 
p1.week = "weekday" and 
p2.week = "weekend"