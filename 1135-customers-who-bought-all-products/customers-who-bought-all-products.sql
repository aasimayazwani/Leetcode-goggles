with cte as 
(select *, count(distinct product_key)  as "total"
from customer 
group by customer_id )

select distinct customer_id from cte 
where total in (select count(distinct product_key) from product) ; 