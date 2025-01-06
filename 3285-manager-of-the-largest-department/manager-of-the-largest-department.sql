with cte as
    (select *
        from
        (select
            *, 
            dense_rank() over (order by counting desc) as "ranking"
            from
                (select 
                dep_id, count(distinct emp_id) as "counting"
                from employees
                group by dep_id) as t1) as t2 
        where ranking = 1 )

select 
p2.emp_name as "manager_name", p1.dep_id 
from cte as p1 
inner join employees as p2
on 
p1.dep_id = p2.dep_id 
where p2.position = "Manager" 
order by dep_id asc ; 