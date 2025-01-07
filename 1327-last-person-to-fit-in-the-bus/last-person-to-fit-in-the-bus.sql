select person_name from
    (select person_name, total_weight
        from
        (select *, sum(weight) over (order by turn) as "total_weight"
        from queue ) as t1 
        where total_weight <= 1000 ) as t2 
    order by total_weight desc 
    limit 1 ; 
    