with cte as
    (select 
    product_id, 
    year(purchase_date) as "year_value",
    count(distinct order_id) as "counting"
    from orders
    group by product_id, year_value )

select distinct t1.product_id from cte as t1, cte as t2 
where 
t1.product_id = t2.product_id and 
t1.year_value - t2.year_value = 1 and 
t1.counting >=3 and t2.counting >= 3 ; 