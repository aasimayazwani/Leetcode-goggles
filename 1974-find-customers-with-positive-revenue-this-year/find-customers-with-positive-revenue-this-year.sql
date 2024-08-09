# Write your MySQL query statement below
select customer_id from 
(select customer_id, sum(revenue) as "total"
from customers 
where year = 2021
group by customer_id, year) as t1 
where total > 0 ;