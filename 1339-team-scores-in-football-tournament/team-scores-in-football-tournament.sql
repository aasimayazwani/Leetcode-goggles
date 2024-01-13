with cte as 
(select 
match_id, 
host_team, 
guest_team, 
case 
    when host_goals > guest_goals then 3
    when host_goals < guest_goals then 0 
    when host_goals = guest_goals then 1 
    end 
    as "host_score",

case 
    when guest_goals > host_goals then 3
    when guest_goals < host_goals then 0 
    when guest_goals = host_goals then 1 
    end 
    as "guest_score" 
from matches )

select teams.team_id, 
teams.team_name, 
ifnull(df2.num_points,0) as "num_points"
from teams 
left join 
(select team as "team_id" , sum(score) as "num_points"
from 
(select host_team as "team", host_score as "score" from cte 
UNION ALL 
select guest_team as "team", guest_score as "score" from cte) as df1
group by team_id ) as df2
on teams.team_id = df2.team_id 
order by num_points desc , team_id asc ;  