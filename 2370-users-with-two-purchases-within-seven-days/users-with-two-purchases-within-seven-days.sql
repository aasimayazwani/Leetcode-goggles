# Write your MySQL query statement below
select distinct t1.user_id from purchases as t1, 
    purchases as t2 
    where 
    t1.purchase_id != t2.purchase_id and 
    t1.user_id = t2.user_id and 
    abs(datediff(t2.purchase_date,t1.purchase_date)) <= 7 
    order by user_id asc ; 