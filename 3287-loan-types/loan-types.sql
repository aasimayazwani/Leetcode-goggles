# Write your MySQL query statement below
select distinct t1.user_id from loans as t1, 
        loans as t2
        where 
        t1.loan_type = "Refinance" and 
        t2.loan_type = "Mortgage"  and 
        t1.user_id = t2.user_id 
        order by user_id asc ; 