"""
Part 3 - Advanced

ORM 을 활용해 titanic.txt 데이터를 옮겨봅니다.

아래 Base 와 engine, DATABASE_URI, Passenger 데이터베이스 클래스 등을 통해 데이터베이스를 확인합니다.

추가 코드 작성은 자유롭게 해줍니다.

테스트 코드에서는 테이블 이름이 'Passenger' 인 것을 확인하니 유의하시길
바라겠습니다.
"""
from csv import DictReader
import csv
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, Session

### 아래 코드는 변경하지 말아주세요! ###
DATABASE_URI = "sqlite:///titanic_orm.db"
CSV_FILEPATH = 'titanic.txt'

engine = create_engine(DATABASE_URI)
Base = declarative_base(bind=engine)
session = Session(bind=engine)
### 위 코드는 변경하지 말아주세요! ###

class Passenger(Base):
    __tablename__ = 'Passenger'
    survived = Column(Integer)
    pclass = Column(Integer)
    name = Column(String(15),primary_key=True)
    sex = Column(String(6))
    age = Column(Integer)
    ss = Column(Integer)
    pc =Column(Integer)
    fare=Column(Integer)

Base.metadata.create_all(bind=engine)

    
def insert_passenger(survived,pclass,name,sex,age,ss,pc,fare):
    data = Passenger(survived=survived, pclass=pclass,name=name,sex=sex, age=age, ss=ss,pc=pc, fare=fare)
    session.add(data)
    session.commit()


with open('C:/Users/user/Desktop/ai/ds-sa-orm/titanic.txt','r') as csvfile:
     reader = csv.DictReader(csvfile)
     for i in reader:
         insert_passenger(list(i.values())[0], list(i.values())[1] ,list(i.values())[2] ,list(i.values())[3] ,list(i.values())[4] ,list(i.values())[5] ,list(i.values())[6],list(i.values())[7])

