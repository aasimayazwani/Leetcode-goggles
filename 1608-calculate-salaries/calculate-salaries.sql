# Write your MySQL query statement below
with cte as
(select *, max(salary) over (partition by company_id) as "max_salary"
from salaries)

select company_id, employee_id, employee_name, round(salary,0) as "salary"
from
(select company_id, employee_id, employee_name, 
case 
    when max_salary < 1000 then salary
    when max_salary >= 1000 and max_salary <= 10000 then salary - salary*0.24
    when max_salary > 10000 then salary - salary*0.49
    end 
    as "salary"
from cte) as t5 
