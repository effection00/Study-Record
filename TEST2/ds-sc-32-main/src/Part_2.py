from sqlalchemy import Column, Integer, String
import sqlalchemy

if sqlalchemy.__version__[:3] == "1.4":
    from sqlalchemy.orm import declarative_base
else:
    from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

"""
Part 2

Animal 이라는 클래스를 만들어 
ORM 테이블을 만들어 봅니다.
"""

class Animal(Base):
    __tablename__ = ''

    id = Column(Integer)
