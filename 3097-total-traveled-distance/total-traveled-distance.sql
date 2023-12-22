# Write your MySQL query statement below
with cte as
(select user_id, sum(distance) as "travelled_distance" from rides 
group by user_id)

select users.user_id, users.name, ifnull(cte.travelled_distance,0) as 'traveled distance' from users
left join cte 
on cte.user_id = users.user_id 
order by users.user_id ; 