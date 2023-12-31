select t1.user_id, ifnull(sum(t1.quantity*t2.price),0) as "spending"  from sales as t1
inner join 
product as t2 
on t1.product_id = t2.product_id 
group by t1.user_id 
order by spending desc, user_id asc ;