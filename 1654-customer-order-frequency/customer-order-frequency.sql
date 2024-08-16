with cte as
    (select
    t1.product_id, t2.customer_id, 
    date_format(t2.order_date,"%Y-%m") as "month",
    sum(t1.price*t2.quantity) as "total"
    from product as t1 
    inner join 
    orders as t2 
    on t1.product_id = t2.product_id 
    group by t2.customer_id, month)

select t4.customer_id, t3.name  from customers as t3 
    inner join 
    (select t1.customer_id  
    from cte as t1, cte as t2 
    where t1.customer_id = t2.customer_id and 
    t1.total >= 100 and t2.total >= 100  and 
    t1.month = "2020-06" and t2.month = "2020-07") as t4 
    on t3.customer_id = t4.customer_id ; 