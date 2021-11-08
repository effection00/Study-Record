# Sprint Challenge 31x

# Part 1 Docker container 실행과 명령 전달

## docker container에 저장된 환경변수 PART_1 을 찾아내세요

- 이미지 생성자 : `aibcontents`
- 이미지 이름 : `sc31`
- 태그 : `1.0`
- 환경변수 출력 명령 : `env`

# Part 2.1 데이터베이스 생성

## schema.png 와 동일하게 데이터베이스를 생성합니다.

> Hint : 각 테이블에서 id 가 primary key 입니다.

구현해야 하는 테이블 목록은 다음과 같습니다:

- User
- Product
- User_Product

# Part 2.2 The Northwind Database

- 아래는 northwind_small의 ER (Entity-Relationship) 다이어그램입니다. Microsoft Access로 만들어졌기 때문에 테이블 및 필드명이 다를 수 있습니다.

  ![Imgur](https://i.imgur.com/QoAU8j5.png)

- 아래의 코드로 DB내 모든 테이블들의 이름을 확인할 수 있습니다

  ```sql
  -- northwind_small 내의 모든 table들의 이름을 불러옵니다 --
  SELECT name
    FROM sqlite_master
  WHERE type='table'
  ORDER BY name;
  ```

- 주의: ER 다이어그램과 달리 실제 데이터베이스의 테이블들은 모두 단수형입니다 (s가 붙지않습니다). 각 테이블들의 schema는 다음의 코드로 확인 가능합니다

  ```sql
  -- Customer 테이블 schema 확인--
  SELECT sql FROM sqlite_master WHERE name="Customer";
  ```

## 아래의 조건에 맞는 쿼리문을 작성하세요

> 모든 문제는 SQL 만을 사용해서 풀어주세요.

1. 데이터베이스에서 가장 비싼 제품 (개별 가격당) 10개를 불러오세요
   - id, 제품이름
2. 고용 당시 직원의 평균 연령은 몇살인가요?
3. 1번 문제에 제품을 만든 회사들도 같이 출력하세요
4. 가장 많은 제품이 있는 카테고리를 출력하세요
5. 각 도시별로 직원의 평균 연령이 어떻게 다른가요?
6. 어느 직원이 가장 많은 영역을 차지하고 있나요?
