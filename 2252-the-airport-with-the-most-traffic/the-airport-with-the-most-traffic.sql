with cte as 
    ((select departure_airport as "airport_id", flights_count
    from flights)
    union all 
    (select arrival_airport as "airport_id", flights_count
    from flights))

select airport_id from
    (select airport_id, dense_rank() over (order by total desc) as "ranking" from
        (select airport_id, sum(flights_count) as "total"
        from cte 
        group by airport_id ) as p1 ) as p2 
    where ranking = 1 