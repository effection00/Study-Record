from src import Part_2 as p2
from src.Part_1 import Customer, Address, Item, Invoice_Item


class TestInsertion:
    def test_insert_customer(self, db_session, customer_data):
        data = customer_data

        for d in data:
            p2.insert_customer(
                customer_id=d['customer_id'],
                customer_name=d['customer_name'],
                customer_age=d['customer_age'],
                session=db_session
            )

        assert db_session.query(Customer).count() == len(data)

        for test_data in data:
            test_query = db_session.query(Customer)\
                .where(Customer.customer_id == test_data['customer_id'])\
                .one()

            assert test_query.customer_id == test_data['customer_id']
            assert test_query.customer_name == test_data['customer_name']
            assert test_query.customer_age == test_data['customer_age']

    def test_insert_address(self, db_session, address_data):
        data = address_data

        for d in data:
            p2.insert_address(
                address_id=d['address_id'],
                city=d['city'],
                street=d['street'],
                customer_id=d['customer_id'],
                session=db_session
            )

        assert db_session.query(Address).count() == len(data)

        for test_data in data:
            test_query = db_session.query(Address)\
                .where(Address.address_id == test_data['address_id'])\
                .one()

            assert test_query.address_id == test_data['address_id']
            assert test_query.city == test_data['city']
            assert test_query.street == test_data['street']
            assert test_query.customer_id == test_data['customer_id']

    def test_insert_item(self, db_session, item_data):
        data = item_data

        for d in data:
            p2.insert_item(
                item_id=d['item_id'],
                item_name=d['item_name'],
                item_price=d['item_price'],
                session=db_session
            )

        assert db_session.query(Item).count() == len(data)

        for test_data in data:
            test_query = db_session.query(Item)\
                .where(Item.item_id == test_data['item_id'])\
                .one()

            assert test_query.item_id == test_data['item_id']
            assert test_query.item_name == test_data['item_name']
            assert test_query.item_price == test_data['item_price']

    def test_insert_invoice_item(self, db_session, invoices_data):
        data = invoices_data

        for d in data:
            p2.insert_invoice_item(
                ii_id=d['ii_id'],
                invoice_date=d['invoice_date'],
                address_id=d['address_id'],
                item_id=d['item_id'],
                session=db_session
            )

        assert db_session.query(Invoice_Item).count() == len(data)

        for test_data in data:
            test_query = db_session.query(Invoice_Item)\
                .where(Invoice_Item.ii_id == test_data['ii_id'])\
                .one()

            assert test_query.ii_id == test_data['ii_id']
            assert test_query.invoice_date == test_data['invoice_date']
            assert test_query.address_id == test_data['address_id']
            assert test_query.item_id == test_data['item_id']


class TestDeletion:
    def test_delete_customer(self, db_data_session):
        def count_func(t): return db_data_session.query(t).count()
        table = Customer
        test_id = 1
        # when given a customerID
        # remove all related to customer
        # remove address, remove invoice_item
        current_count = count_func(table)

        p2.delete_customer(customer_id=test_id, session=db_data_session)
        final_count = count_func(table)

        assert final_count == current_count - 1

        customer_address_count = db_data_session.query(Address)\
            .where(Address.customer_id == test_id)\
            .count()

        invoices_count = db_data_session.query(Customer)\
            .join(Address, Customer.customer_id == Address.customer_id)\
            .join(Invoice_Item,
                  Address.address_id == Invoice_Item.address_id)\
            .where(Customer.customer_id == test_id)\
            .count()

        assert customer_address_count == 0
        assert invoices_count == 0

    def test_delete_item(self, db_data_session):
        def count_func(t): return db_data_session.query(t).count()
        # when given item_id
        # remove invoice item as well
        table = Item
        test_id = 1

        current_count = count_func(table)

        p2.delete_item(item_id=test_id, session=db_data_session)
        final_count = count_func(table)

        assert final_count == current_count - 1

        invoices_count = db_data_session.query(Invoice_Item)\
            .where(Invoice_Item.item_id == test_id)\
            .count()

        assert invoices_count == 0

    def test_delete_address(self, db_data_session):
        def count_func(t): return db_data_session.query(t).count()

        # when given address_id
        table = Address
        test_id = 1

        current_count = count_func(table)

        p2.delete_address(address_id=test_id, session=db_data_session)
        final_count = count_func(table)

        assert final_count == current_count - 1

        invoices_count = db_data_session.query(Invoice_Item)\
            .where(Invoice_Item.address_id == test_id)\
            .count()

        assert invoices_count == 0


class TestUpdate:
    def test_update_customer_name(self, db_data_session):
        test_id = 1
        test_name = "new name"

        p2.update_customer_name(customer_id=test_id, new_name=test_name,
                                session=db_data_session)

        new_customer = db_data_session.query(Customer)\
            .where(Customer.customer_id == test_id)\
            .one()

        assert new_customer.customer_name == test_name

    def test_update_item_price(self, db_data_session):
        test_id = 1
        test_price = 8275

        p2.update_item_price(item_id=test_id, new_price=test_price,
                             session=db_data_session)

        new_item = db_data_session.query(Item)\
            .where(Item.item_id == test_id)\
            .one()

        assert new_item.item_price == test_price


class TestRead:
    def test_read_customer_items_names(self, db_data_session):
        test_id = 1
        expected_items = ['Books', 'Tissue']

        items = p2.read_customer_item_names(customer_id=test_id,
                                            session=db_data_session)

        assert items.sort() == expected_items.sort()

    def test_read_item_invoices_date(self, db_data_session, invoices_data):
        test_id = 1
        expected_invoices = [ii["invoice_date"] for ii in invoices_data if
                             ii["ii_id"] == test_id]

        invoices = p2.read_item_invoices_date(item_id=test_id,
                                              session=db_data_session)

        assert invoices.sort() == expected_invoices.sort()

    def test_read_customer_addresses_city(self, db_data_session, address_data):
        test_id = 1
        expected_addresses = [a["city"] for a in address_data if
                              a["address_id"] == test_id]

        addresses = p2.read_customer_addresses_city(customer_id=test_id,
                                                    session=db_data_session)

        assert addresses.sort() == expected_addresses.sort()
