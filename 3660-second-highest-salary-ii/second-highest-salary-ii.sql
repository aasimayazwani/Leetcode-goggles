# Write your MySQL query statement below
select emp_id, dept 
    from
    (select *, 
        dense_rank() over (partition by dept order by salary desc) as "ranking"
        from employees) as t1 
    where ranking = 2 
    order by emp_id asc ; 