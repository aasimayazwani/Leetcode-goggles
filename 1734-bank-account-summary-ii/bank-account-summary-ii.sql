# Write your MySQL query statement below
with cte as
(select * from (select account, sum(amount) as "amount" from transactions 
group by account) as t1 
where amount > 10000 )

select t2.name, cte.amount as "balance" from cte inner join 
users as t2 
on cte.account  = t2.account ; 