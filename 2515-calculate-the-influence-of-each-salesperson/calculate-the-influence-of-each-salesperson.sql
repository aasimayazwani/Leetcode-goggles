with cte as 
(select salesperson_id, sum(price) as "total"
from 
(select t1.salesperson_id, t2.price from customer as t1 
inner join 
sales as t2 
on t1.customer_id = t2.customer_id 
) as t3 
group by t1.salesperson_id)

select
t4.salesperson_id, 
t4.name, 
ifnull(t5.total,0) as "total" 
from salesperson as t4 
left join 
cte as t5 
on t4.salesperson_id = t5.salesperson_id 