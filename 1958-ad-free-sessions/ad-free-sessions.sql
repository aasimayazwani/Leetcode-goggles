with cte as (select distinct t1.session_id from playback as t1 
inner join 
ads as t2 
on t1.customer_id = t2.customer_id 
where t2.timestamp >= t1.start_time and t2.timestamp <= t1.end_time)

select session_id from playback where
session_id not in (select session_id from cte); 