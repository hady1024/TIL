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

-- 2. 나이 그룹이 10(age)미만인 사람의 수를 출력하시오.
SELECT COUNT(*) FROM healthcare WHERE age < 10;
-- COUNT(*)
--------
-- 156277

-- 3. 성별이 1인 사람의 수를 출력하시오.
SELECT COUNT(*) FROM healthcare WHERE gender = 1;
-- COUNT(*)
--------
-- 510689

-- 4. 흡연 수치(smoking)가 3이면서 음주(is_drinking)가 1인 사람의 수를 출력하시오.
SELECT COUNT(*) FROM healthcare WHERE smoking = 3 and is_drinking = 1;
-- COUNT(*)
--------
-- 150361

-- 5. 양쪽 시력이(va_left, va_right) 모두 2.0이상인 사람의 수를 출력하시오.
SELECT COUNT(*) FROM healthcare WHERE va_left >= 2.0 and va_right >= 2.0;
-- COUNT(*)
--------
-- 2614

-- 6. 시도(sido)를 모두 중복 없이 출력하시오.
SELECT DISTINCT sido FROM healthcare;

-- 36
-- 27
-- 11
-- 31
-- 41
-- 44
-- 48
-- 30
-- 42
-- 43
-- 46
-- 28
-- 26
-- 47
-- 45
-- 29
-- 49

-- 자유문제
-- 1. 몸무게가 70 이상인 사람 출력
SELECT COUNT(*) FROM healthcare WHERE weight >= 70;
-- COUNT(*)
--------
-- 335286

-- 2. 혈압이 130 이상인 사람 출력
SELECT COUNT(*) FROM healthcare WHERE blood_pressure >= 130;
-- COUNT(*)
--------
-- 385792

-- 3. 나이가 10미만이고 키가 165이하이며 몸무게 50초과인 사람 출력
SELECT COUNT(*) FROM healthcare WHERE age < 10 and height <= 165 and weight > 50;
-- COUNT(*)
--------
-- 61629

