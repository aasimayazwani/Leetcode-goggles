# Write your MySQL query statement below
with cte as
    (select department, salary
        from
        (select *, 
            dense_rank() over (partition by department order by salary desc) as "ranking"
            from salaries) as t1 
        where ranking =1)

select abs(t1.salary - t2.salary) as "salary_difference"
from cte as t1, cte as t2 
where 
t1.department = "Marketing" and t2.department = "Engineering" ; 