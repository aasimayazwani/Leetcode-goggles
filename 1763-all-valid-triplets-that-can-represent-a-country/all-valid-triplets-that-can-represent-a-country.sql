# Write your MySQL query statement below
with cte as 
(select *, "schoola" as "school" from schoola
union all
select *, "schoolb" as "school" from schoolb
union all
select *, "schoolc" as "school" from schoolc)

select distinct t1.student_name as "member_A",
        t2.student_name as "member_B",
        t3.student_name as "member_C"
        from cte as t1, cte as t2, cte as t3 
where t1.school = "schoola" and 
        t2.school = "schoolb" and 
        t3.school = "schoolc" and 
        t1.student_name != t2.student_name and 
        t2.student_name != t3.student_name and  
        t1.student_name != t3.student_name and  
        t1.student_id != t2.student_id and
        t1.student_id != t3.student_id and 
        t2.student_id != t3.student_id ;