# Write your MySQL query statement below
with cte as
    (select 
    t1.project_id, t2.employee_id, t2.experience_years
    from project as t1 inner join 
    employee as t2 on t1.employee_id = t2.employee_id )

select project_id, employee_id from
    (select *, 
        dense_rank() over (partition by project_id order by experience_years desc) as "ranking"
        from cte) as t3 
    where ranking = 1 