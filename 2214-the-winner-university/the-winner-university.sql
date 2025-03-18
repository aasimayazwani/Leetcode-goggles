# Write your MySQL query statement below
with cte as
    (select "New York University" as "uni", sum(score) as "total"
        from
        (select case 
            when score >= 90 then 1 
            else 0 
            end as "score"
            from newyork) as t1), 

cte2 as
    (select "California University" as "uni", sum(score) as "total"
        from
        (select case 
            when score >= 90 then 1 
            else 0 
            end as "score"
            from California) as t2),

cte3 as
    (select * from cte 
    union all 
    select * from cte2 )

select 
    case 
        when CA > NY then "California University"
        when CA < NY then "New York University"
        else "No Winner"
    end as "winner"
    from        
    (select  
    p1.total as "NY", p2.total as "CA"
    from cte3 as p1, cte3 as p2 
    where p1.uni = "New York University" and 
        p2.uni = "California University") as R1 ; 
