CREATE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select count(distinct user_id)
      from Purchases
      where time_stamp >= startDate and time_stamp <= endDate and amount >= minAmount
      
  );
END
