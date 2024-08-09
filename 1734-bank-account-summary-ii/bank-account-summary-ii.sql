# Write your MySQL query statement below
with cte as
(select name,account,  amount
from 
(select t1.name,t1.account, t2.amount from users as t1 
inner join 
transactions as t2 
on t1.account = t2.account) as t3 )

select name as "NAME", sum(amount) as "BALANCE"
from cte 
group by name 
having BALANCE > 10000; 