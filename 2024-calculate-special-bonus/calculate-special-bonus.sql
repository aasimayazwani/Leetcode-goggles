# Write your MySQL query statement below
select employee_id,
case when left(name,1) != "M" and employee_id%2 != 0 then salary
else 0 
end as "bonus"
from Employees
order by employee_id asc  ; 