# Write your MySQL query statement below
SELECT EI.unique_id,E.name
FROM Employees as E left join EmployeeUNI as EI ON E.id=EI.id

