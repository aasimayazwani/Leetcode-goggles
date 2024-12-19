# Write your MySQL query statement below
select customer_id 
    from 
    (select customer_id, year, sum(revenue) as "total"
    from Customers
    group by customer_id, year)
    as t1 
where total > 0 and year = 2021 ; 