# Write your MySQL query statement below
with cte as
(select employee_id, sum(ceil((unix_timestamp(out_time)- unix_timestamp(in_time))/60)) 
as "minutes"
from logs
group by employee_id)

select employee_id from
(select t1.employee_id from employees as t1 
left join cte as t2 
on 
t1.employee_id = t2.employee_id
where t1.needed_hours*60 > t2.minutes) as s1
UNION ALL 
(select distinct employee_id from employees where employee_id not 
in (select distinct employee_id from logs))