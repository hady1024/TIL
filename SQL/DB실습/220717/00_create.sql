-- 테이블 만들기
CREATE TABLE healthcare (
id PRIMARY KEY,
sido INTEGER NOT NULL,
gender INTEGER NOT NULL,
age INTEGER NOT NULL,
height INTEGER NOT NULL,
weight INTEGER NOT NULL,
waist REAL NOT NULL,
va_left REAL NOT NULL,
va_right REAL NOT NULL,
blood_pressure INTEGER NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);

-- csv import 하기
.mode csv 
.import health.csv healthcare

-- Column 출력 설정
.headers on 
.mode column

-- table 및 스키마 조회
.tables
healthcare

.schema healthcare
CREATE TABLE healthcare (
id PRIMARY KEY,        
sido INTEGER NOT NULL, 
gender INTEGER NOT NULL,
age INTEGER NOT NULL,  
height INTEGER NOT NULL,
weight INTEGER NOT NULL,
waist REAL NOT NULL,   
va_left REAL NOT NULL, 
va_right REAL NOT NULL,

blood_pressure INTEGER 
NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);

-- 1. 추가되어 있는 모든 데이터의 수를 출력하시오.
SELECT COUNT(*) FROM healthcare;
-- COUNT(*)
--------
-- 1000000

-- 2. 연령 코드(age)의 최대, 최소 값을 모두 출력하시오.
SELECT MAX(age), MIN(age) FROM healthcare WHERE age;
-- MAX       MIN
-------     -------
-- 18         19

-- 3. 신장(height)과 체중(weight)의 최대, 최소 값을 모두 출력하시오.
SELECT MAX(height), MIN(height), MAX(weight), MIN(weight) FROM healthcare WHERE height and weight;
-- MAX       MIN        MAX         MIN
-------     -------    -------     -------
-- 195        130        135        30

-- 4. 신장(height)이 160이상 170이하인 사람은 몇 명인지 출력하시오.
SELECT COUNT(height) FROM healthcare WHERE height >= 160 and height <= 170;
-- COUNT(height)
----------------
-- 516930

-- 5. 음주(is_drinking)를 하는 사람(1)의 허리 둘레(waist)를 높은 순으로 5명 출력하시오.
SELECT waist FROM healthcare WHERE is_drinking = 1 and not waist = '' ORDER BY waist DESC LIMIT 5; 
-- waist
--------
-- 146.0
-- 142.0
-- 141.4
-- 140.0
-- 140.0

-- 6. 시력 양쪽(va_left, va_right)이 1.5이상이면서 음주(is_drinking)를 하는 사람의 수를 출력하시오.
SELECT COUNT(is_drinking) FROM healthcare WHERE va_left >= 1.5 and va_right >= 1.5 and is_drinking = 1;
-- COUNT(is_drinking)
---------------------
-- 36697

-- 7. 혈압(blood_pressure)이 정상 범위(120미만)인 사람의 수를 출력하시오.
SELECT COUNT(blood_pressure) FROM healthcare WHERE blood_pressure < 120;
-- COUNT(blood_pressure)
------------------------
-- 360808

-- 8. 혈압(blood_pressure)이 140이상인 사람들의 평균 허리둘레(waist)를 출력하시오.
SELECT AVG(waist) FROM healthcare WHERE blood_pressure >= 140;
-- AVG(waist)
--------------
-- 85.8665098512525

-- 9. 성별(gender)이 1인 사람의 평균 키(height)와 평균 몸무게(weight)를 출력하시오.
SELECT AVG(height), AVG(weight) FROM healthcare WHERE gender = 1;
-- AVG(height)      AVG(weight)
---------------     ---------------
-- 167.452735422145    69.7131620222875

-- 10. 키가 가장 큰 사람 중에 두번째로 무거운 사람의 id와 키(height), 몸무게(weight)를 출력하시오.
SELECT id, height, weight FROM healthcare ORDER BY height DESC LIMIT 1;
-- id     height     weight
------    ------     ------
-- 8832    195         95

-- 11. BMI가 30이상인 사람의 수를 출력하시오. 
SELECT



-- 12. 흡연(smoking)이 3인 사람의 BMI지수가 제일 높은 사람 순서대로 5명의 id와 BMI를 출력하시오.
SELECT


------ 자유문제 --------------------

-- 1. 음주(is_drinking)를 하는 사람(1)의 허리 둘레(waist)를 낮은 순으로 5명 출력하시오.
SELECT waist FROM healthcare WHERE is_drinking = 1 and not waist = '' ORDER BY waist ASC LIMIT 5;
-- waist
--------
-- 5.8
-- 8.2
-- 8.7
-- 41.0
-- 49.0 

-- 2. 성별(gender)이 1인 사람의 평균 혈압(blood_pressure)와 평균 몸무게(weight)를 출력하시오.
SELECT AVG(blood_pressure), AVG(weight) FROM healthcare WHERE gender = 1;
-- AVG(blood_pressure)      AVG(weight)
----------------------      ---------------
-- 167.452735422145         69.7131620222875

-- 3. 시력 양쪽(va_left, va_right)이 1.0이상이면서 음주(is_drinking)를 하는 사람의 수를 출력하시오.
SELECT COUNT(is_drinking) FROM healthcare WHERE va_left >= 1.0 and va_right >= 1.0 and is_drinking = 1;
-- COUNT(is_drinking)
---------------------
-- 239238