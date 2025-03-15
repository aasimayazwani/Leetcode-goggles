# Write your MySQL query statement below
with cte as
    (select product_id from sales 
    where sale_date between "2019-01-01" and "2019-03-31" 
    and product_id not in (
        select product_id from sales 
        where sale_date not between "2019-01-01" and "2019-03-31" 
    ))

select distinct p1.product_id, p2.product_name from cte as p1 
inner join 
product as p2 
on p1.product_id = p2.product_id 