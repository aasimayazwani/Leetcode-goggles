with cte as 
(select dept_id, count(distinct student_id) as "student_number"
from student
group by dept_id) 

select t1.dept_name, ifnull(cte.student_number,0) as "student_number" from department as t1 
left join cte 
on 
t1.dept_id = cte.dept_id 
order by cte.student_number desc, dept_name asc ; 