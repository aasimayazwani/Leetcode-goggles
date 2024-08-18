CREATE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select count(distinct user_id) as "user_cnt" 
      from purchases 
      where amount > minAmount and 
      time_stamp between startDate and endDate 
      
  );
END