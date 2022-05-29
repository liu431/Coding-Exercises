# Write your MySQL query statement below
## For each task, generate subtask id from 1 to subtasks_count
## Exclude ids that have been executed
WITH RECURSIVE CTE AS (
    SELECT task_id, subtasks_count
    FROM Tasks
    UNION ALL
    SELECT task_id, subtasks_count - 1
    FROM CTE
    WHERE subtasks_count > 1
)
SELECT task_id , subtasks_count AS subtask_id  
FROM cte
WHERE (task_id , subtasks_count) NOt IN (SELECT * FROM Executed)
