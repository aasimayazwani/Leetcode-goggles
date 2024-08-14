with cte as 
(select  
t1.user_id, t1.product_id, sum(t1.quantity*t2.price) as 'total'
from sales as t1 
inner join product as t2 
on t1.product_id = t2.product_id 
group by t1.user_id, t2.product_id)

select user_id, product_id from 
(select *, dense_rank() over (partition by user_id order by total desc ) as "ranking"
from cte) as t4 
where ranking = 1 ; 