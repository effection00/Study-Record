"""
Part 3

클라우드 데이터베이스에 'passenger' 라는 테이블을 생성하고 titanic.csv 에 있는 데이터를 'passenger' 테이블로 옮깁니다.

passenger 테이블의 필드는 데이터에 알맞게 추가합니다 (필드명은 자유입니다).
아래에는 각 필드에 해당하는 데이터 타입입니다.
- Survived: INT
- Pclass: INT
- Name: VARCHAR(128)
- Sex: VARCHAR(12)
- Age: FLOAT
- Siblings/Spouses Aboard: INT
- Parents/Children Aboard: INT
- Fare: FLOAT

다 옮긴 뒤에 'passenger' 테이블이 있는 데이터베이스 정보를 아래 입력합니다.

아래 psycopg2.connect 를 이용해 connection 변수가 데이터베이스와 연결할 수 있도록 다음 변수들에 알맞은 정보를 담습니다:

- host: 데이터베이스 호스트 주소를 입력합니다.
- user: 데이터베이스 유저 정보를 입력합니다.
- password: 데이터베이스 비밀번호를 입력합니다.
- database: 데이터베이스 이름을 입력합니다.
"""

          
 #=> 도전과제 할 때 따옴표를 제거해주세요
import psycopg2



# 아래 변수들의 명칭을 변경하면 테스트가 정상 작동 안할 수 있습니다.
host = 'rosie.db.elephantsql.com'
user = 'bdbddxqs'
password = '5vXAQrPnYtYmab5UvC86_uYaEB9_xNlX'
database = 'bdbddxqs'

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=database
)


