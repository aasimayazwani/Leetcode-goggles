# Write your MySQL query statement below
with cte as (select * from (select account, sum(amount) as "balance"
from Transactions 
group by account ) as t1 
where balance > 10000)

select t1.name, t2.balance from users as t1 
inner join 
cte as t2 
on t1.account = t2.account ;  