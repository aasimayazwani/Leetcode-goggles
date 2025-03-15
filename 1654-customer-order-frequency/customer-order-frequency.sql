# Write your MySQL query statement below
with cte as
    (select customer_id, 
        sum(price) as "total", 
        date_value
        from
            (select 
            t2.customer_id, 
            t1.price*t2.quantity as "price", 
            date_format(order_date,"%Y-%m") as "date_value"
            from product as t1 inner join orders as t2 on 
            t1.product_id = t2.product_id ) as t3 
        group by customer_id, date_value),

cte2 as
    (select distinct p1.customer_id from cte as p1, cte as p2
    where p1.customer_id = p2.customer_id and 
    p1.date_value = "2020-06" and p2.date_value = "2020-07" and 
    p1.total >= 100 and p2.total >= 100)

select 
q2.customer_id, q2.name 
from cte2 as q1 
inner join 
customers as q2 on 
q1.customer_id = q2.customer_id ; 