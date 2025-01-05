# Write your MySQL query statement below
with cte as
    (select city, peak_calling_hour, count(*) as "number"
        from
        (select hour(call_time) as "peak_calling_hour",
                city
                from calls) as t1 
        group by city, peak_calling_hour)

select city, peak_calling_hour, number as "number_of_calls"
    from
    (select city, peak_calling_hour, number,
            dense_rank() over (partition by city order by number desc)
            as "ranking"
            from cte ) as t2 
    where ranking = 1 
    order by peak_calling_hour desc, city desc ; 