# Write your MySQL query statement below
select abs(max(t1.salary) - max(t2.salary)) as "salary_difference" from salaries as t1 
inner join salaries as t2
on t1.department = "Engineering" and 
t2.department = "Marketing" ; 