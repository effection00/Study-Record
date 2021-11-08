import pytest
from dateutil import parser
from src.Part_1 import Address, Customer, Item, Invoice_Item


@pytest.fixture
def db_data_session(db_session, customer_data, address_data,
                    invoices_data, item_data):

    for d in address_data:
        db_session.add(
            Address(
                address_id=d["address_id"],
                customer_id=d["customer_id"],
                city=d["city"],
                street=d["street"]
            )
        )

    for d in customer_data:
        db_session.add(
            Customer(
                customer_id=d["customer_id"],
                customer_name=d["customer_name"],
                customer_age=d["customer_age"]
            )
        )

    for d in item_data:
        db_session.add(
            Item(
                item_id=d["item_id"],
                item_name=d["item_name"],
                item_price=d["item_price"]
            )
        )

    for d in invoices_data:
        db_session.add(
            Invoice_Item(
                ii_id=d["ii_id"],
                item_id=d["item_id"],
                address_id=d["address_id"],
                invoice_date=d["invoice_date"]
            )
        )

    db_session.commit()

    yield db_session


@pytest.fixture
def customer_data():
    data = [
        {
            "customer_id": 1,
            "customer_name": "Po",
            "customer_age": 5,
        },
        {
            "customer_id": 2,
            "customer_name": "Chopper",
            "customer_age": None,
        }
    ]
    return data


@pytest.fixture
def item_data():
    data = [
        {
            "item_id": 1,
            "item_name": "Books",
            "item_price": 100,
        },
        {
            "item_id": 2,
            "item_name": "Tissue",
            "item_price": 1000,
        },
        {
            "item_id": 3,
            "item_name": "Soccerball",
            "item_price": 500,
        }
    ]
    return data


@pytest.fixture
def address_data():
    data = [
        {
            "address_id": 1,
            "city": "Seoul",
            "street": "Cloud Street",
            "customer_id": 1
        },
        {
            "address_id": 2,
            "city": "IceCave",
            "street": "CaveRoad 101",
            "customer_id": 1
        },
        {
            "address_id": 3,
            "city": "GreenLand",
            "street": "Bricky Road",
            "customer_id": 2
        }
    ]
    return data


@pytest.fixture
def invoices_data():
    data = [
        {
            "ii_id": 1,
            "invoice_date": parser.parse("2020-02-26 11:50:12.704041"),
            "address_id": 1,
            "item_id": 1
        },
        {
            "ii_id": 2,
            "invoice_date": parser.parse("2020-01-26 08:50:12.704041"),
            "address_id": 1,
            "item_id": 2
        },
        {
            "ii_id": 3,
            "invoice_date": parser.parse("2020-12-20 11:50:12.704041"),
            "address_id": 2,
            "item_id": 1
        },
        {
            "ii_id": 4,
            "invoice_date": parser.parse("2020-08-16 11:50:12.704041"),
            "address_id": 3,
            "item_id": 2
        },
        {
            "ii_id": 5,
            "invoice_date": parser.parse("2020-09-22 11:50:12.704041"),
            "address_id": 3,
            "item_id": 3
        }
    ]
    return data
