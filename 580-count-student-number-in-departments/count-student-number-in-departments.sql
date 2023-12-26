# Write your MySQL query statement below
with cte as
(select dept_id, count(student_id) as "counting" from student 
group by dept_id )

select t2.dept_name, ifnull(t1.counting,0) as "student_number" from department as t2 
left join 
cte as t1 
on t1.dept_id = t2.dept_id 
order by student_number desc, dept_name asc ; 