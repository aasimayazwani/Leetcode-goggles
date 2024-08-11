# Write your MySQL query statement below
select employee_id, team_size from 
(select *, count(team_id) over (partition by team_id) as "team_size"
from employee
) as t1 
