# Write your MySQL query statement below
with cte as
    (select managerId from
        (select managerId, count(*) as "total"
        from employee
        group by managerId ) as t1 
        where total >= 5)

select p2.name from cte as p1 
inner join employee as p2 
on p1.managerid = p2.id 