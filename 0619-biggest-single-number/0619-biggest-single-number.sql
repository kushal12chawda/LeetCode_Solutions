/* Write your PL/SQL query statement below */
WITH UniqueNumbers AS (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
)
SELECT MAX(num) AS num
FROM UniqueNumbers;
