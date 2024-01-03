# Write your MySQL query statement below
with cte as (select user_id, 
case 
    when action = "confirmed" then 1 
    when action = "timeout" then 0 
    else 0 
    end 
as "something"
from confirmations)


select signups.user_id, ifnull(t5.confirmation_rate,0) as "confirmation_rate" from signups 
left join
(select user_id, round(total/counting,2) as "confirmation_rate" from
(select *, count(user_id) over (partition by user_id) as "counting",
sum(something) over (partition by user_id) as "total"
from cte) as t4 
group by user_id) as t5  
on 
t5.user_id = signups.user_id ; 

