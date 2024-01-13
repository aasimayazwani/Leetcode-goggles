# Write your MySQL query statement below
with cte as 
(select distinct student_id from exam where student_id not in
(select distinct student_id from 
(select *, dense_rank() over (partition by exam_id order by score desc ) as "highest"
        , dense_rank() over (partition by exam_id order by score asc ) as "lowest"
        from exam) as t1 
        where highest = 1 or 
        lowest = 1)) 

select cte.student_id, student.student_name  
from cte 
inner join student
on cte.student_id = student.student_id 
order by cte.student_id asc ; 