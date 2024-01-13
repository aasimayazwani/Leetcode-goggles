# Write your MySQL query statement below
with cte as 
(select t1.employee_id from employees as t1 
inner join 
salaries as t2 
on t1.employee_id = t2.employee_id) 

select employee_id from 
(select employee_id from employees 
where employee_id not in (select employee_id from cte)
UNION 
select employee_id from salaries 
where employee_id not in (select employee_id from cte))
as t5 
order by employee_id asc ; 