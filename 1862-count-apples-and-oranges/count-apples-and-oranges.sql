SELECT 
    SUM(t1.apple_count + IFNULL(t2.apple_count, 0)) AS apple_count,
    SUM(t1.orange_count + IFNULL(t2.orange_count, 0)) AS orange_count
FROM 
    boxes AS t1 
LEFT JOIN 
    chests AS t2 
ON 
    t1.chest_id = t2.chest_id;
