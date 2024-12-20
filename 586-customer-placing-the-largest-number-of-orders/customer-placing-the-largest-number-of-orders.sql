# Write your MySQL query statement below
with cte as 
(select customer_number, count(order_number) as "counting"
from orders
group by customer_number)

select customer_number from
(select *, dense_rank() over (order by counting desc) as "ranking"
from cte )  as t1 
where ranking = 1 ; 