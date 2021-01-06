# Write your MySQL query statement below
update salary as s set s.sex = 
case s.sex 
    when "f" then "m" 
    when "m" then "f"
    else s.sex 
end ;