with cte as
(select * from actions 
where action_date = "2019-07-04" and 
action = "report" and extra is not null)

select extra as "report_reason",count(distinct post_id) as "report_count"
from cte 
group by extra 