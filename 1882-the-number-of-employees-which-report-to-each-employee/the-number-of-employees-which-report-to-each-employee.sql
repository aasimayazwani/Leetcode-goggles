with cte as 
(select employee_id, reports_count, average_age
    from
    (select reports_to as "employee_id", count(distinct employee_id) as "reports_count", round(avg(age),0) as "average_age"
    from employees
    where reports_to is not null
    group by reports_to) as t1 )

select t1.employee_id, t2.name, t1.reports_count, t1.average_age from cte as t1 
inner join 
employees as t2 
on t1.employee_id = t2.employee_id 
order by t1.employee_id asc ; 