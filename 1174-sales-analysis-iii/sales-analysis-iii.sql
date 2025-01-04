# Write your MySQL query statement below
with cte as
    (select 
    t2.product_id, t1.product_name, 
    t2.sale_date 
    from product as t1 
    inner join 
    sales as t2 
    on 
    t1.product_id = t2.product_id) 

select 
    distinct product_id, product_name 
    from 
        cte 
    where sale_date between "2019-01-01" and "2019-03-31"
    and product_id not in 
        (select product_id from cte 
        where sale_date < "2019-01-01" or sale_date > "2019-03-31") ; 