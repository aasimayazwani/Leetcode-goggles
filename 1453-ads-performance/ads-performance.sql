# Write your MySQL query statement below
with cte as 
    (select
        ad_id, user_id, 
        case 
            when action = "Clicked" then 1 
            when action = "Viewed" then 0
        end 
        as "action"
        from
        (select ad_id, user_id, action 
        from ads 
        where action != "Ignored") as a1),


results as
(select ad_id, round(100*(sum(action)/count(action)),2) as "ctr"
from cte 
group by ad_id)

select distinct t1.ad_id, ifnull(t2.ctr,0) as "ctr"
from ads as t1
left join 
results as t2
on t1.ad_id = t2.ad_id
order by  ctr desc, ad_id asc 