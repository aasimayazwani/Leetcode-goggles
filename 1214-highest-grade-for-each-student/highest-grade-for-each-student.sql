select student_id, course_id, grade from 
(select *, dense_rank() over (partition by student_id order by grade desc, course_id asc) as ranking
from enrollments) as t1 
where ranking = 1 
order by student_id asc ; 