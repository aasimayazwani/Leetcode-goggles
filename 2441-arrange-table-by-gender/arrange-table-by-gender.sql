with cte as (select *, dense_rank() over (partition by gender order by user_id asc ) as "ranking", 
case 
    when gender = "male" then 3 
    when gender = "female" then 1 
    when gender = "other" then 2 
end 
    as "sub_rankings"
from genders )

select user_id, gender from cte 
order by ranking asc, sub_rankings asc ; 