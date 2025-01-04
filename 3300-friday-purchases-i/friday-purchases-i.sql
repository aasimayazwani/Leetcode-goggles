# Write your MySQL query statement below
with cte as
(select weeknumber, purchase_date, sum(amount_spend) as "total_amount" from
    (select *,
        date_format(purchase_date,"%w") as "weekday",
        ceil(date_format(purchase_date,"%d")/7) as "weeknumber",
        date_format(purchase_date,"%Y-%m") as "month"
        from purchases) as t1 
        where weekday = 5
        group by weeknumber)

select 
weeknumber as "week_of_month", purchase_date , total_amount
from 
cte 
order by week_of_month asc ;