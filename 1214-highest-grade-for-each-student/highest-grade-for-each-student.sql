with cte as 
(select * from 
(select *,dense_rank() over (partition by student_id order by grade desc, course_id asc ) as "ranking"
 from enrollments 
) as t1 
where ranking = 1 )

select student_id,course_id,grade from cte 
order by student_id asc ; 