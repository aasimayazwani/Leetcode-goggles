# Write your MySQL query statement below
select 
t1.sale_date, t1.sold_num - t2.sold_num as "diff"
from 
sales as t1, sales as t2 
where 
t1.sale_date = t2.sale_date and 
t1.fruit = "apples" and 
t2.fruit = "oranges" 
order by sale_date asc ; 