with cte as (select t1.apple_count + ifnull(t2.apple_count,0) as "apple_count",
        t1.orange_count + ifnull(t2.orange_count,0) as "orange_count"
 from boxes as t1 
left join chests as t2 
on t1.chest_id = t2.chest_id )

select sum(apple_count) as "apple_count",
        sum(orange_count) as "orange_count"
        from cte ; 