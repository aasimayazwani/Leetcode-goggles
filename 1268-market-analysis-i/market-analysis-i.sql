with cte as
    (select buyer_id, count(order_id)  as "counting"
    from orders
    where year(order_date) = 2019 
    group by buyer_id )

select 
t1.user_id as "buyer_id",
t1.join_date, 
ifnull(t2.counting,0) as "orders_in_2019" 
from users as t1 
left join 
cte as t2 
on 
t1.user_id = t2.buyer_id ; 