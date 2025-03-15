/* Write your PL/SQL query statement below */
SELECT
  Manager.employee_id,
  Manager.name,
  COUNT(Employee.employee_id) AS reports_count,
  ROUND(AVG(Employee.age)) AS average_age
FROM Employees Manager  -- Removed AS for table alias
INNER JOIN Employees Employee
  ON Employee.reports_to = Manager.employee_id
GROUP BY Manager.employee_id, Manager.name  -- Explicitly group by columns
ORDER BY Manager.employee_id;
