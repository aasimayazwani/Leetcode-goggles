# Write your MySQL query statement below
with cte as
    (select order_id, product_id, tim, count(order_id) as "total"
        from
        (select order_id, product_id, quantity, year(purchase_date) as "tim"
        from orders) as t1 
    group by product_id, tim)

select distinct t2.product_id  from cte as t2, cte as t3 
where t2.tim - t3.tim = 1 and 
t2.total >= 3 and t3.total >= 3 and 
t2.product_id = t3.product_id ; 