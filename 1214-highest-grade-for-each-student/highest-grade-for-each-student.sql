with cte as 
(select *, dense_rank() over (partition by student_id order by grade desc, course_id asc ) as "ranking"
from enrollments)

select student_id, course_id, grade from cte 
where ranking = 1 
order by student_id asc ; 