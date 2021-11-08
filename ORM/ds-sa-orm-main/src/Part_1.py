"""
Part 1

ORM 으로 테이블을 만들어 봅니다.

Part 1 에서 테이블을 어떻게 구현하는지에 따라 Part 2 함수들이 영향을 받을 수도
있습니다. 데이터베이스를 리셋해야 하는 경우를 위해 따로 'reset_db' 가 추가되어
있습니다.

> pass 를 삭제하고 함수 기능을 구현하는 코드를 작성해줍니다.
"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,\
    DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql.operators import custom_op

DATABASE_URI = 'sqlite:///orm.db'
engine = create_engine(DATABASE_URI)
Base = declarative_base()

def reset_db(engine=engine):
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


class Address(Base):
    __tablename__ = 'Address'
    address_id = Column(Integer, primary_key=True)
    city = Column(String(48))
    street = Column(String(128))
    customer_id = Column(Integer,ForeignKey('Customer.customer_id'))


class Item(Base):
    __tablename__ = 'Item'
    item_id = Column(Integer, primary_key=True)
    item_name = Column(String(32),nullable=False)
    item_price = Column(Integer)


class Invoice_Item(Base):
    __tablename__ = 'Invoice_Item'
    ii_id = Column(Integer, primary_key=True)
    invoice_date = Column(DateTime, nullable=False)
    address_id = Column(Integer,ForeignKey('Address.address_id'))
    item_id = Column(Integer, ForeignKey('Item.item_id'))


class Customer(Base):
    __tablename__ = 'Customer'
    customer_id = Column(Integer, primary_key=True)
    customer_name = Column(String(32), nullable=False)
    customer_age = Column(Integer)


