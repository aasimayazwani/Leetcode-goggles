# Write your MySQL query statement below
with cte as
    (select reports_to as "employee_id", 
            count(*) as "reports_count",
            round(avg(age)) as "average_age"
            from employees
            where reports_to is not null
            group by reports_to
            )

select t1.employee_id, t2.name , t1.reports_count, t1.average_age from cte as t1 
inner join employees as t2 
on t1.employee_id = t2.employee_id
order by employee_id asc ; 