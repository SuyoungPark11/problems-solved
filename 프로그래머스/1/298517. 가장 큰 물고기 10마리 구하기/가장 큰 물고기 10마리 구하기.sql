-- 코드를 작성해주세요
select ID, LENGTH
from FISH_INFO
order by IFNULL(LENGTH, 10) DESC, ID
limit 10
