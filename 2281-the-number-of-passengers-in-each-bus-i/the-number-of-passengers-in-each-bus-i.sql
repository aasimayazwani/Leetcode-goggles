with cte as
(select bus_id,  lag(arrival_time,1,0) over (order by arrival_time) as "previous",
        arrival_time as "departure"
        from buses)

select t1.bus_id, ifnull(count(distinct t2.passenger_id),0) as "passengers_cnt" from cte as t1 
left join 
passengers as t2 
on 
t2.arrival_time > t1.previous and t2.arrival_time <= t1.departure
group by t1.bus_id 
order by t1.bus_id asc ; 