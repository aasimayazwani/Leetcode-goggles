# Write your MySQL query statement below
with cte as (
        select query_name, round(avg(rating/position),2) as "quality" 
        from queries
        group by query_name),

query as
(select query_name, round(100*(query_percentage/total),2) as "query_percentage"
from
    (select query_name, 
        sum(case 
            when rating < 3 then 1 
            else 0 
        end)
        as "query_percentage",
        count(*) as "total"
        from queries
        group by query_name) as t1 )
    

select cte.query_name, cte.quality, query.query_percentage as "poor_query_percentage" from cte 
inner join 
query 
on 
cte.query_name = query.query_name ; 