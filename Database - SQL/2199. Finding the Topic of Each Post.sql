# Write your MySQL query statement below
# REGEXP_LIKE(expr, pat[, match_type])
SELECT
  P.post_id,
  COALESCE(GROUP_CONCAT(DISTINCT K.topic_id ORDER BY K.topic_id), 'Ambiguous!') as topic
FROM
  Posts P
  LEFT JOIN Keywords K ON REGEXP_LIKE(P.content, CONCAT('\\b', K.word, '\\b'), 'i')
GROUP BY
  P.post_id;
