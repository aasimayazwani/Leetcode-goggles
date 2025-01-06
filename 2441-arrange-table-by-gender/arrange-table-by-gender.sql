with cte1 as
(select *, 
    row_number() over (order by user_id) as "ranking",
    0 as "actual"
    from
    (select * from genders 
    where gender = "female"
    order by user_id asc) as t1 ),

cte2 as
(select *, 
    row_number() over (order by user_id) as "ranking",
    1 as "actual"
    from
    (select * from genders 
    where gender = "other"
    order by user_id asc) as t1 ),

cte3 as
(select *, 
    row_number() over (order by user_id) as "ranking",
    2 as "actual"
    from
    (select * from genders 
    where gender = "male"
    order by user_id asc) as t1 )

select user_id, gender
    from
    (select * from cte1
    union all
    select * from cte2
    union all
    select * from cte3) as p1 
order by ranking asc, actual asc ; 