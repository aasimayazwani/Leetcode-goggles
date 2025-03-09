# Write your MySQL query statement below
with cte as
    (select project_id, count(employee_id) as "counting"
    from project
    group by project_id)

select project_id
    from
    (select *, dense_rank() over (order by counting desc) as "ranking"
    from cte) as t1 
    where 
    ranking = 1 ; 