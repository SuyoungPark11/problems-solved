-- 코드를 입력하세요
SELECT DATETIME AS 시간
FROM ANIMAL_INS
WHERE 
    DATETIME = (SELECT MAX(DATETIME) FROM ANIMAL_INS);
