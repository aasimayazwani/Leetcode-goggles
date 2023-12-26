# Write your MySQL query statement below
select product_id, year as "first_year", quantity, price from 
(select *, dense_rank() over (partition by product_id order by year asc) 
as "ranking"
from sales ) as t1 
where ranking = 1 ;