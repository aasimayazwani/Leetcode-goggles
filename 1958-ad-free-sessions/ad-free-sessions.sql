select session_id from playback 
where 
session_id not in
    (select t1.session_id
    from  ads as t2 
    left join 
    playback as t1 
    on 
    t1.customer_id = t2.customer_id and 
    t2.timestamp >= t1.start_time and 
    t2.timestamp <= t1.end_time) ;