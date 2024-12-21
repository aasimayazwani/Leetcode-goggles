# Write your MySQL query statement below
select 
t1.symbol as "metal", t2.symbol as "nonmetal"
from elements as t1, elements as t2 
where 
t1.type = "Metal" and t2.type = "Nonmetal" 