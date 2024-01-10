# Write your MySQL query statement below
select week_of_month, purchase_date, sum(amount_spend) as "total_amount"
from 
(select 
round(day(purchase_date)/7,0) +1 as "week_of_month",
date_format(purchase_date,"%W") as "day_",
purchase_date,
amount_spend 
from 
purchases 
having day_ = "Friday") as t1
group by week_of_month 
order by week_of_month asc ; 