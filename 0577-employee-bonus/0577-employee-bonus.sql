/* Write your PL/SQL query statement below */
SELECT Employee.name, Bonus.bonus
FROM Employee
LEFT JOIN Bonus
ON Employee.empId = Bonus.empId
WHERE NVL(Bonus.bonus, 0) < 1000;