# Write your MySQL query statement belowselect 
# class > count of students > filter for >=5 
select class 
    from
        (select class, count(distinct student) as "counting"
        from courses
        group by class )
            as t1 
    where counting >= 5 ; 
