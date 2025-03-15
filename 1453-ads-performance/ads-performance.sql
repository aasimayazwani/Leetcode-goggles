# Write your MySQL query statement below
with cte as
    (select ad_id, 
        case when action = "Clicked" then 1 
        else 0 
        end as "clicked",
        case when action = "Clicked" then 1 
        when action = "Viewed" then 1 
        else 0 
        end as "total"
        from ads)

select ad_id, ifnull(round(100*(sum(Clicked)/sum(total)),2),0) as "ctr"
from cte 
group by ad_id 
order by ctr desc, ad_id asc ; 