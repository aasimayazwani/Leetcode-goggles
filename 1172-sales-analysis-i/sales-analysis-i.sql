select seller_id from
    (select seller_id, dense_rank() over (order by total desc) as "ranking"
    from
    (select seller_id, sum(price) as "total"
    from sales
    group by seller_id) as t1) as t2 
    where ranking = 1  ; 
