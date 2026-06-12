# Write your MySQL query statement below
with topthree as(
    select name,salary,departmentId, 
    DENSE_RANK()over(partition by departmentId order by salary desc) as rnk from Employee
)
select d.name as Department , tt.name as Employee,tt.salary as Salary from topthree tt join Department d on tt.departmentId=d.id where tt.rnk<=3 
