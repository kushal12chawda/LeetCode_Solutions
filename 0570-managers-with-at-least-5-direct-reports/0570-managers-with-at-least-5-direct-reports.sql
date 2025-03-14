/* Write your PL/SQL query statement below */
SELECT Manager.name
FROM Employee
INNER JOIN Employee Manager
ON Employee.managerId = Manager.id
GROUP BY Manager.id, Manager.name
HAVING COUNT(*) >= 5;
