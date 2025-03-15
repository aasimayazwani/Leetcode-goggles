# Write your MySQL query statement below

with cte as (
    select *, count(employee_id) over (partition by employee_id) as "counting"
    from employee
)

(select employee_id, department_id from cte
    where counting > 1 and primary_flag = "Y")
union all 
(select employee_id, department_id from cte
    where counting = 1)
