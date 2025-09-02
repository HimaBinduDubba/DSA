# Write your MySQL query statement below
SELECT p.product_name,s.year,s.price FROM Sales as S left join Product as p on S.product_id=p.product_id
