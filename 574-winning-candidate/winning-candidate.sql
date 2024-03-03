with cte as
(select t1.name as "name",ifnull(t2.counting,0) as "counting" 
from candidate as t1 
left join
(select candidateid as "candidateid", count(candidateid) as "counting"
from vote
group by candidateid) as t2 
on t1.id = t2.candidateid) 

select name from
(select *, dense_rank() over (order by counting desc, name desc ) as "ranking" from cte )
as t3 
where ranking = 1 