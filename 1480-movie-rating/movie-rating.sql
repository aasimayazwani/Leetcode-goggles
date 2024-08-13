# Write your MySQL query statement below
with cte as 
(select name from
(select 
t1.user_id, t1.name, t2.counting
from users as t1 inner join 
(select user_id, count(distinct movie_id) as "counting"
from movierating
group by user_id ) as t2 
on t1.user_id = t2.user_id 
order by counting desc, name asc  ) as t3 
limit 1 )

select name as "results" from cte 
union all
(select title from 
(select t4.title, avg(t5.rating) as "avg_rating" 
from movies as t4 inner join 
movierating as t5 
on 
t4.movie_id = t5.movie_id 
where date_format(Created_at,"%Y-%m")= "2020-02"
group by t4.title
order by avg_rating desc, t4.title asc limit 1) as t6 ) 