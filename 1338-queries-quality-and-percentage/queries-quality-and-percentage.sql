# Write your MySQL query statement below
select query_name,  
    round(avg(quality),2) as "quality", 
    round(100*(sum(low)/count(*)),2) as "poor_query_percentage" 
    from
    (select query_name, result, 
        rating/position as "quality", 
        case 
            when rating < 3 then 1 
            else 0 
        end as "low"
        from queries) as p1 
    group by query_name 