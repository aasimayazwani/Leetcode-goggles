# Write your MySQL query statement below
# 
# table > unique subjects

select distinct teacher_id, count(distinct subject_id) as "cnt"
from teacher
group by teacher_id; 
