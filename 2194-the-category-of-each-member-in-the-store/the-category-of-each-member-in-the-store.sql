with cte as
(select *, 
case 
    when charged_amount > 0 then 1 
    when charged_amount = 0 then 0 
end 
as "number_of_purchases"
from
(select  
t1.visit_id, t1.member_id, t1.visit_date, ifnull(t2.charged_amount,0) as "charged_amount"
from visits as t1 
left join 
purchases as t2 
on 
t1.visit_id = t2.visit_id) as t3) 

select t7.member_id, 
        t7.name, 
        ifnull(t6.category, "Bronze") as "category"
 from members as t7 
left join 
(select member_id, 
case when conversion >= 80 then "Diamond"
        when conversion >= 50 and conversion < 80 then "Gold"
        when conversion < 50 then "Silver"
end as "category"
from
(select member_id, (sum(number_of_purchases)*100)/(count(number_of_purchases))
as "conversion"
from cte 
group by member_id) as t5) as t6 
on t7.member_id = t6.member_id 