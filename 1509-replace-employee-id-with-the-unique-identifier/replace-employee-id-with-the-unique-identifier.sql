# Write your MySQL query statement below
SELECT eU.unique_id, e.name
FROM Employees AS e
LEFT JOIN EmployeeUNI AS eU
ON e.id = eU.id;
