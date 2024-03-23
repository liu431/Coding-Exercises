# Write your MySQL query statement below
#: A literal hash character.
# [A-Za-z0-9_]+: One or more (+) characters that are either a letter (A-Za-z), a digit (0-9), or an underscore (_).
select 
    REGEXP_SUBSTR(tweet, '#[A-Za-z0-9]+') as hashtag,
    count(1) as hashtag_count
from Tweets 
where year(tweet_date) = 2024 and month(tweet_date) = 2
group by 1
order by 2 desc, 1 desc
limit 3
