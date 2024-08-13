with cte as 
(select dept_id, count(distinct student_id) as "student_number"
from student
group by dept_id)

select t1.dept_name, ifnull(t2.student_number,0) as "student_number" from department as t1 
left join 
cte as t2 
on t1.dept_id = t2.dept_id
order by t2.student_number desc, t1.dept_name asc ; 
