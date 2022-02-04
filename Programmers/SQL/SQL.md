# SELECT

### 모든 레코드 조회하기

ANIMAL_INS 테이블에서 모든 컬럼을 가져온 뒤 ANIMAL_ID 순으로 정렬해서 조회하기( * 전체 조회하기)

```
SELECT * FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```



### 역순 정렬하기

ANIMAL_INS 테이블에서 NAME과 DATETIME 컬럼을 ANIMAL_ID 역순으로 조회하기(DESC : 내림차순)

```
SELECT NAME, DATETIME FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC
```



### 아픈 동물 찾기

ANIMAL_INS 테이블에서 아픈 동물의 아이디와 이름을 조회하는 SQL문 작성하기

결과는 아이디 순으로 조회

```
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'
```



### 어린 동물 찾기

ANIMAL_INS 에서 젊은 동물의 아이디와 이름을 조회하는 SQL문 작성하기

젊은 동물은 INTAKE_CONDITION 이 'Aged'가 아닌 것

```
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION <> 'Aged'
```



### 동물의 아이디와 이름

ANIMAL_INS 에서 모든 동물의 아이디와 이름을 ANIMAL_ID 순으로 조회하는 SQL문 작성하기

```
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```



### 여러 기준으로 정렬하기

ANIMAL_INS 에서 모든 동물의 아이디와 이름, 보호 시작일을 이름 순으로 조회하는 SQL문 작성하기. 단, 이름이 같은 동물 중에서는 보호를 나중에 시작한 동물을 먼저 보여주기

```
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```



### 상위 n개 레코드

ANIMAL_INS 에 가장 먼저 들어온 동물의 이름을 조회하는 SQL문 작성하기

(정렬 하고 몇개 보여주는지로 생각해보자)

```
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1
```



# SUM, MAX, MIN



### 최댓값 구하기

가장 최근에 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성하기

AS 뒤에는 출력할 컬럼명

```
SELECT DATETIME AS 시간
FROM ANIMAL_INS
ORDER BY DATETIME DESC
LIMIT 1
```



### 최솟값 구하기

동물 보호소에 가장 먼저 들어온 동물은 언제 들어왔는지 조회하는 SQL문을 작성하기

```
SELECT DATETIME AS 시간
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1
```



### 동물 수 구하기

동물 보호소에 동물이 몇 마리 들어왔는지 조회하는 SQL문 작성하기

```
SELECT COUNT(*)
FROM ANIMAL_INS
```



### 중복 제거하기  (어렵다)

동물 보호소에 들어온 동물의 이름은 몇 개인지 조회하는 SQL문을 작성하기.

이때 이름이 NULL 인 경우는 집계하지 않고 중복되는 이름은 하나로 친다.

SQ1은 서브쿼리의 이름

```
SELECT COUNT(*)
FROM 
    (
    SELECT NAME
    FROM ANIMAL_INS
    WHERE NAME IS NOT NULL
    GROUP BY NAME
    ) SQ1
```



### 고양이와 개는 몇 마리 있을까 (어렵다)

동물보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL문을 작성하기. 고양이를 개보다 먼저 조회하기

-> 동물 보호소에 들어온(`FROM ANIMAL_INS`) 동물 중 고양이와 개가 각각(`GROUP BY ANIMAL_TYPE`) 몇 마리인지(`COUNT(ANIMAL_TYPE)`) 조회하는(`SELECT`) SQL문을 작성하라.
-> 이 때, 고양이를 개보다 먼저(`ORDER BY`) 조회하라.
-> c가 d보다 사전순으로 앞서 있으므로 `ORDER BY` 의 default값인 `ASC`로 설정.

```
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS count
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE
```



### 동명 동물 수 찾기

동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하는 SQL문을 작성해주세요. 이때 결과는 이름이 없는 동물은 집계에서 제외하며, 결과는 이름 순으로 조회해주세요.

-> 동물 보호소에 들어온(`FROM ANIMAL_INS`) 동물 이름 중(`GROUP BY`) 두 번 이상 쓰인 이름과(`HAVING COUNT(NAME) > 1`) 해당 이름이 쓰인 횟수(`COUNT(NAME)`)를 조회하는(`SELECT`) SQL문을 작성하라.
-> 이 때, 결과는 이름이 없는 동물은 집계에서 제외하며, 결과는 이름 순으로(`ORDER BY`) 조회하라.

```
SELECT NAME, COUNT(NAME) AS COUNT
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME) > 1
ORDER BY NAME
```



### 입양 시각 구하기(1)

보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.

```
SELECT HOUR(DATETIME) AS HOUR, COUNT(DATETIME) AS COUNT
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) >= 9
    AND HOUR(DATETIME) <= 19
GROUP BY HOUR(DATETIME)
ORDER BY HOUR
```



### 입양 시각 구하기(2)

보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.

```
SET @hour := -1; -- 변수 선언

SELECT (@hour := @hour + 1) AS HOUR,
(SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hour) AS COUNT
FROM ANIMAL_OUTS
WHERE @hour < 23
```

