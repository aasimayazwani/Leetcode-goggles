# Write your MySQL query statement below
with cte as
    (select *, row_number() over (order by topping_name asc ) as "ranking"
        from
        (select * from toppings order by topping_name asc) as t1)

select 
concat(t1.topping_name,",",t2.topping_name,",",t3.topping_name) as "pizza", t1.cost+t2.cost+t3.cost as "total_cost"
from 
cte as t1, cte as t2, cte as t3
where 
t1.topping_name != t2.topping_name and 
t2.topping_name != t3.topping_name and 
t1.topping_name != t3.topping_name and
t1.ranking < t2.ranking and 
t2.ranking < t3.ranking and 
t1.ranking < t3.ranking 
order by total_cost desc, pizza asc ;