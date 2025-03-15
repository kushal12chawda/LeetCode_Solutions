/* Write your PL/SQL query statement below */
WITH Players AS (
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
)
SELECT ROUND(
    (SELECT COUNT(DISTINCT P.player_id)
     FROM Players P
     INNER JOIN Activity A
     ON P.player_id = A.player_id
     AND A.event_date = P.first_login + 1
    ) / 
    (SELECT COUNT(DISTINCT player_id) FROM Activity), 
    2
) AS fraction
FROM DUAL;
