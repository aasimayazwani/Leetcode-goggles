# Write your MySQL query statement below
select t1.sale_date, t1.sold_num - t2.sold_num
as "diff" from sales as t1 
inner join sales as t2 
on t1.sale_date = t2.sale_date 
where t1.fruit = "apples"
and 
t2.fruit = "oranges"
order by sale_date asc ; 