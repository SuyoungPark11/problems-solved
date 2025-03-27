-- 코드를 작성해주세요
select count(*) AS COUNT
from ECOLI_DATA
where 1=1
    and (GENOTYPE & 2) != 2
    and ((GENOTYPE & 4) = 4 OR (GENOTYPE & 1) = 1)