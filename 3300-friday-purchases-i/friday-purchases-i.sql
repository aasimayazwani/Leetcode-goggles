# Write your MySQL query statement below
select week_of_month, purchase_date, sum(amount_spend) as "total_amount"
    from 
    (select ceil(days/7) as "week_of_month",
    purchase_date, 
    amount_spend 
    from
        (select *, 
        date_format(purchase_date,"%d") as "days",
        date_format(purchase_date,"%W") as "weekday" from purchases) as t1
    where weekday = "Friday") as t2 
    group by week_of_month
    order by week_of_month asc ; 
