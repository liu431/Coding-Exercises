# Write your MySQL query statement below
# Report all the sessions that did not get shown any ads
# Results are the sessions that not matched with ads
SELECT session_id
FROM Playback
LEFT JOIN Ads ON Playback.customer_id = Ads.customer_id AND 
(Ads.timestamp >= Playback.start_time AND Ads.timestamp <= Playback.end_time)
WHERE Ads.customer_id IS NULL
