# Write your MySQL query statement below
select *, rank() over (order by points desc) as "position"
    from
    (select team_id, team_name, 3*wins + draws as "points"
    from teamstats) as t1 
order by points desc, team_name asc ;