# Write your MySQL query statement below
(SELECT name,population,area FROM World Where area>=3000000) Union  (SELECT name,population,area FROM World Where population>=25000000);
