# Write your MySQL query statement below
with cte as
    (select 
    t1.project_id, 
    t1.employee_id, 
    t2.experience_years
    from project as t1 
    left join 
    employee as t2 
    on 
    t1.employee_id = t2.employee_id)

select 
project_id, round(avg(experience_years),2) as "average_years"
 from cte 
 group by project_id