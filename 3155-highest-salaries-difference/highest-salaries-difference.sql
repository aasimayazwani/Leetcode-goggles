# Write your MySQL query statement below
with cte as 
(select * from
(select *, dense_rank() over (partition by department order by salary desc) as "ranking"
from salaries) as t1 
where ranking = 1 )

select abs(t3.salary-t2.salary) as "salary_difference" from cte as t2 , 
cte as t3 
where t2.department = "Engineering" and 
t3.department = "Marketing"