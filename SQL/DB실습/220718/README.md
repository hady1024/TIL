###  1. 흡연 여부(smoking)로 구분한 각 그룹의 컬렴명과 그룹의 사람의 수를 출력하시오.

```sql 
SELECT smoking,COUNT(*) FROM healthcare GROUP BY smoking;
-- smoking  COUNT(*)
-------  --------
-- 1        626138
-- 2        189808
-- 3        183711
--          343
```

###  2. 음주 여부(is_drinking)로 구분한 각 그룹의 컬렴명과 그룹의 사람의 수를 출력하시오.

```sql 
SELECT is_drinking, COUNT(*) FROM healthcare GROUP BY is_drinking;
-- is_drinking    COUNT(*)
--------------    --------
-- 0              415119
-- 1              584685
--                196
```

### 3. 음주 여부로 구분한 각 그룹에서 혈압(blood_pressure)이 200이상인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE blood_pressure >= 200 GROUP BY is_drinking; 
-- COUNT(*)
--------
-- 6064
-- 1770
```

### 4. 시도(sido)에 사는 사람의 수가 50000명 이상인 시도의 코드와 그 시도에 사는 사람의 수를 출력하시오.

```sql
SELECT COUNT(*),sido FROM healthcare GROUP BY sido HAVING COUNT(sido) >= 50000;
-- COUNT(*)  sido
-----------  -------
-- 166231    11
-- 69025     26
-- 58345     28
-- 247369    41
-- 54438     47
-- 68530     48
```

### 5. 키(height)를 기준으로 구분하고, 각 키와 사람의 수를 출력하시오.

> 단, 사람의 수를 기준으로 내림차순으로 5개까지 출력하시오.

```sql
SELECT height, COUNT(*) FROM healthcare GROUP BY height ORDER BY COUNT(*) DESC LIMIT 5;
-- height  COUNT(*)
-- ------  --------
-- 160     184993
-- 155     181306
-- 165     179352
-- 170     152585
-- 150     128555
```

### 6. 키(height)와 몸무게(weight)를 기준으로 구분하고, 몸무게와, 키, 해당 그룹의 사람의 수를 출력하시오. 

> 단, 사람의 수를 기준으로 내림차순 5개까지 출력하시오.

```sql
SELECT weight, height, COUNT(*) FROM healthcare GROUP BY height, weight ORDER BY COUNT(*) DESC LIMIT 5;
-- weight height COUNT(*)
-- ------  ------  --------
-- 55      155     45866
-- 60      160     42454
-- 65      165     40385
-- 50      155     38582
-- 55      160     38066
```

### 7. 음주여부에 따라 평균 허리둘레(waist)와 사람의 수를 출력하시오.

```sql 
SELECT avg(waist), COUNT(*) FROM healthcare GROUP BY is_drinking;
-- AVG(waist)        COUNT(*)
-- ----------------  --------
-- 81.2128249971711  415119
-- 83.1541594191841  584685
-- 82.7714285714286  196
```

### 8. 각 성별(gender)의 평균 왼쪽 시력(va_left)과 평균 오른쪽 시력(va_right)를 출력하시오.

> 단, 평균 왼쪽 시력과 평균 오른쪽 시력의 컬럼명을 '평균 왼쪽 시력' '평균 오른쪽 시력'로 표시하고, 평균 시력은 소수점 둘째 자리까지 출력하시오.

```sql
SELECT ROUND(AVG(va_left),2)"평균 왼쪽 시력",ROUND(AVG(va_right),2)"평균 오른쪽 시력" FROM healthcare GROUP BY gender;
-- 평균 왼쪽 시력  평균 오른쪽 시력
-- --------  ---------
-- 0.98      0.99
-- 0.88      0.88
```

### 9. 각 나이대(age)의 평균 키와 평균 몸무게를 출력하시오.

> 단, 평균 키와 평균 몸무게의 컬럼명을 '평균 키' '평균 몸무게'로 표시하고, 평균키가 160 이상 평균 몸무게가 60 이상인 데이터만 출력하시오.

```sql
```

### 10. 음주 여부(is_drinking)와 흡연 여부(smoking)에 따른 평균 BMI를 출력하시오.

> 단, 음주 여부 또는 흡연 여부가 공백이 아닌 행만 사용하세요.

```sql
```