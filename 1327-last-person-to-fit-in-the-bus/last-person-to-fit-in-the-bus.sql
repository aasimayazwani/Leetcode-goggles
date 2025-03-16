# Write your MySQL query statement below
with cte as
    (select person_name, Total_Weight from
        (select person_name, sum(weight) over (order by turn asc) as "Total_Weight"
        from queue) as t1 
        where Total_Weight <= 1000)

select person_name from
    (select *, dense_rank() over (order by Total_Weight desc ) as "ranking" 
    from cte) as t2 
    where ranking = 1 