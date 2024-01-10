# Write your MySQL query statement below
with cte as
(select contest_id, gold_medal as "medal", "GOLD" AS "TYPE" from contests
union all 
select contest_id, silver_medal as "medal", "SILVER" AS "TYPE"  from contests
UNION ALL 
select contest_id, bronze_medal as "medal", "BRONZE" AS "TYPE"  from contests)


select users.name, users.mail from users 
inner join
(select distinct medal from
((select distinct t1.medal from cte as t1, cte as t2 , cte as t3 
#where t2.contest_id - t1.contest_id  =1 
#and t3.contest_id - t2.contest_id= 1
where t1.medal = t2.medal 
and t2.medal = t3.medal and 
t1.contest_id != t2.contest_id and 
t3.contest_id != t2.contest_id  and 
t1.contest_id != t3.contest_id 
and t1.TYPE = "GOLD" 
and t2.TYPE = "GOLD" 
and t3.TYPE = "GOLD") 
UNION ALL  
(select distinct t1.medal from cte as t1, cte as t2 , cte as t3 
where t2.contest_id - t1.contest_id  =1 
and t3.contest_id - t2.contest_id= 1
and t1.medal = t2.medal 
and t2.medal = t3.medal )) as t5) as t6
on users.user_id = t6.medal ; 