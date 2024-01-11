# Write your MySQL query statement below
with cte as 
(select t1.salesperson_id, t1.name, t2.customer_id from salesperson as t1 
left join 
Customer as t2 
on t1.salesperson_id = t2.salesperson_id)

select t3.salesperson_id, t3.name, ifnull(sum(t4.price),0) as "total" from cte as t3 
left join 
sales as t4 
on t3.customer_id =t4.customer_id 
group by t3.salesperson_id