with cte as
(select user_id, visit_date, 
        lead(visit_date,1,"2021-1-1") over (partition by user_id order by visit_date)
        as "next_day"
        from uservisits)

select user_id, max(biggest_window) as "biggest_window"
    from
    (select user_id, abs(datediff(visit_date,next_day)) as "biggest_window" from cte )
    as t1 
    group by user_id 
    order by user_id asc ; 
