with cte as
    (select *, dense_rank() over (order by counting desc) as "forward"
            , dense_rank() over (order by counting asc) as "backward"
        from
        (select activity, count(*) as "counting"
        from friends
        group by activity) as t1)

select distinct activity from friends
where 
activity not in (select distinct activity from cte 
where forward =1 or backward = 1)  ;