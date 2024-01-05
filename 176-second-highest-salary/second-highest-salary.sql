# Write your MySQL query statement below
select 
    ifnull(
        (select salary from
            (select * , 
            dense_rank() over (order by salary desc ) as "Ranking"
            from employee) as t1 
            where ranking = 2 limit 1 )
    ,null) as "SecondHighestSalary"