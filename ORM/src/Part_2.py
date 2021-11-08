from datetime import datetime
from sqlalchemy import select, update,distinct
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import current_time
from src.Part_1 import Address, Customer, Invoice_Item, Item, engine


session = Session(bind=engine)

"""
Part 2

ORM 을 통해 데이터를 추가하는 연습을 진행합니다.

각 함수에는 session 객체를 받도록 되어 있습니다. 해당 세션은 Part 1 에서 구축한
엔진을 기반으로 생성한 세션 객체입니다.

각 함수에서 받는 파라미터를 바탕으로 요구사항에 알맞은 함수 기능들을
구현해주세요.

각 함수의 테스트는 이미 주어진 파라미터를 기반으로 실행하게 됩니다. 하지만 각
테이블에서 Null 값이 될 수 있는 파라미터들은 기본값을 따로 설정해야 테스트를
통과하는 경우도 있습니다.

> pass 를 삭제하고 함수 기능을 구현하는 코드를 작성해줍니다.
"""

def insert_address(customer_id, address_id, city, street,
                   session=session):
    customer = Address(address_id = address_id, city=city,street= street, customer_id=customer_id)
    session.add(customer)
    session.commit()


def insert_invoice_item(item_id, address_id, ii_id, 
                        invoice_date, session=session):
    customer = Invoice_Item(ii_id = ii_id, invoice_date=invoice_date,address_id=address_id, item_id=item_id)
    session.add(customer)
    session.commit()


def insert_item(item_name, item_price=None, item_id=None, session=session):
    customer = Item(item_id=item_id, item_name=item_name, item_price=item_price)
    session.add(customer)
    session.commit()

def insert_customer(customer_name, customer_age,
                    customer_id, session=session):
    customer = Customer(customer_id=customer_id, customer_name=customer_name, customer_age=customer_age)
    session.add(customer)
    session.commit()

def read_item_invoices_date(item_id, session=session):
    date = session.query(Invoice_Item.invoice_date).filter(Invoice_Item.item_id == item_id).all()
    return date

    

def read_customer_addresses_city(customer_id, session=session):
    city = session.query(Address.city).filter(Address.customer_id == customer_id).all()
    return city
  

def read_customer_item_names(customer_id, session=session):
    name = session.query(Item.item_name).filter(Address.customer_id == customer_id).order_by().distinct().all()
    return name


def delete_customer(customer_id, session=session):
    session.query(Customer).filter(Customer.customer_id==customer_id).delete()
    session.query(Address).filter(Address.customer_id==customer_id).delete()
    session.commit()



def delete_item(item_id, session=session):
    session.query(Item).filter(Item.item_id==item_id).delete()
    session.query(Invoice_Item).filter(Invoice_Item.item_id==item_id).delete()
    session.commit()


def delete_address(address_id, session=session):
    session.query(Address).filter(Address.address_id==address_id).delete()
    session.query(Invoice_Item).filter(Invoice_Item.address_id==address_id).delete()
    session.commit()

def update_customer_name(customer_id, new_name, session=session):
    session.query(Customer).filter(Customer.customer_id==customer_id).update({"customer_name":new_name})
    session.commit()

def update_item_price(item_id, new_price, session=session):
    session.query(Item).filter(Item.item_id==item_id).update({"item_price":new_price})
    session.commit()
    
