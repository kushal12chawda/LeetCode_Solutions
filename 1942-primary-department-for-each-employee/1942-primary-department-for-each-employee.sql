/* Write your PL/SQL query statement below */
SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y'
UNION
SELECT employee_id, department_id
FROM Employee e1
WHERE (
    SELECT COUNT(*) FROM Employee e2
    WHERE e1.employee_id = e2.employee_id
) = 1;
