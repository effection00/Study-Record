"""
Part 4

- 클라우드 데이터베이스 작업하기

새로운 몽고DB 클라우드 클러스터 및 데이터베이스를 생성한 뒤에 titanic.csv 에 있는 탑승객 데이터 하나마다 문서로 저장합니다.

필요에 따라 추가로 코드를 작성합니다.

각 값의 데이터 타입은 아래와 같습니다. (필드명은 자유입니다).
아래에는 각 필드에 해당하는 데이터 타입입니다.
- Survived: int
- Pclass: int
- Name: str
- Sex: str
- Age: float
- Siblings/Spouses Aboard: int
- Parents/Children Aboard: int
- Fare: float

다 옮긴 뒤에 'passengers' 데이터베이스 정보를 아래 입력합니다.

아래 connection 변수가 데이터베이스와 연결할 수 있도록 다음 변수들에 알맞은 정보를 담습니다:

- host: 데이터베이스 호스트 주소를 입력합니다.
- user: 데이터베이스 유저 정보를 입력합니다.
- password: 데이터베이스 비밀번호를 입력합니다.
- database_name: 데이터베이스 이름을 입력합니다.
- cluster_name: 클러스터 이름을 입력합니다.

아래 주석을 풀어서 문제를 풀어주세요
"""
# import csv
# import os
# from pymongo import MongoClient

# 아래 변수들의 명칭을 변경하면 테스트가 정상 작동 안할 수 있습니다.

# host = '호스트 주소를 입력해주세요'
# user = '유저 이름을 입력해주세요'
# password = '비밀번호를 입력해주세요'
# database_name = '데이터베이스 이름을 입력해주세요'
# collection_name = '콜렉션 이름을 입력해주세요'

# MONGO_URI = f"mongodb+srv://{user}:{password}@{host}/{database_name}?retryWrites=true&w=majority"

# connection = MongoClient(MONGO_URI)
