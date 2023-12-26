with cte as
(select transaction_id, cur_date, amount from
(select *, date_format(day,"%Y-%m-%d") as cur_date from transactions ) as t1 )

select distinct transaction_id from
(select *, dense_rank() over (partition by cur_date order by amount desc)  as "ranking" from cte) as t2 
where ranking = 1 
order by transaction_id asc ; 