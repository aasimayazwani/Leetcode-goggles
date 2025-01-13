# Write your MySQL query statement below
with cte as
(select customer_number, dense_rank() over (order by counting desc) as "ranking"
    from
    (select customer_number, count(order_number) as "counting"
    from orders 
    group by customer_number) as t1
)

select distinct customer_number from cte 
where ranking =1 ;