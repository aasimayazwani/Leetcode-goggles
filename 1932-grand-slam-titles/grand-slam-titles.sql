with cte as 
(select wimbledon as "wins" from championships
union all
select Fr_open  as "wins" from championships
union all
select US_open  as "wins" from championships
union all
select Au_open  as "wins" from championships),

t1 as
(select wins, count(wins) as "grand_slams_count" from cte 
group by wins) 

select 
t2.player_id, t2.player_name, t1.grand_slams_count 
from players as t2 
inner join 
t1 
on 
t2.player_id = t1.wins ; 