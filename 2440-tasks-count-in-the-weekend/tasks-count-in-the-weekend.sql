with cte as 
(select *, date_format(submit_date,"%W") as "weekday" from tasks)


select count(distinct t1.task_id) as "weekend_cnt",
        count(distinct t2.task_id) as "working_cnt"
        from cte as t1, 
        cte as t2
        where t1.weekday in ("Saturday","Sunday") and 
        t2.weekday not in ("Saturday","Sunday") ; 