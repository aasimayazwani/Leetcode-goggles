# Write your MySQL query statement below
select *, 
    dense_rank() over (partition by season_id order by points desc, goal_difference desc) as "position"
    from
    (select 
    season_id, 
    team_id, 
    team_name
    , 3*wins+draws as "points", 
            goals_for - goals_against as "goal_difference"
            from seasonstats) as t1