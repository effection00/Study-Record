from src import Part_1


class TestAddressTable:

    __tablename__ = 'Address'

    __table__ = Part_1.Address

    __fields__ = [
        {
            "name": "address_id",
            "type": "INTEGER",
            "primary_key": True,
            "nullable": False
        },
        {
            "name": "city",
            "type": "VARCHAR(48)",
            "primary_key": False,
            "nullable": True
        },
        {
            "name": "street",
            "type": "VARCHAR(128)",
            "primary_key": False,
            "nullable": True
        },
        {
            "name": "customer_id",
            "type": "INTEGER",
            "primary_key": False,
            "nullable": True
        }
    ]

    def test_table_exists(self, db_inspector):
        assert db_inspector.has_table(self.__tablename__)

    def test_fields(self):
        for field in self.__fields__:
            field_attr = object.__getattribute__(self.__table__, field['name'])
            assert str(field_attr.type) == field['type']
            assert field_attr.primary_key == field['primary_key']
            assert field_attr.nullable == field['nullable']


class TestInvoiceItemTable:

    __tablename__ = 'Invoice_Item'

    __table__ = Part_1.Invoice_Item

    __fields__ = [
        {
            "name": "ii_id",
            "type": "INTEGER",
            "primary_key": True,
            "nullable": False
        },
        {
            "name": "invoice_date",
            "type": "DATETIME",
            "primary_key": False,
            "nullable": False
        },
        {
            "name": "address_id",
            "type": "INTEGER",
            "primary_key": False,
            "nullable": True
        },
        {
            "name": "item_id",
            "type": "INTEGER",
            "primary_key": False,
            "nullable": True
        }
    ]

    def test_table_exists(self, db_inspector):
        assert db_inspector.has_table(self.__tablename__)

    def test_fields(self):
        for field in self.__fields__:
            field_attr = object.__getattribute__(self.__table__, field['name'])
            assert str(field_attr.type) == field['type']
            assert field_attr.primary_key == field['primary_key']
            assert field_attr.nullable == field['nullable']


class TestItemTable:

    __tablename__ = 'Item'

    __table__ = Part_1.Item
    __fields__ = [
        {
            "name": "item_id",
            "type": "INTEGER",
            "primary_key": True,
            "nullable": False
        },
        {
            "name": "item_name",
            "type": "VARCHAR(32)",
            "primary_key": False,
            "nullable": False
        },
        {
            "name": "item_price",
            "type": "INTEGER",
            "primary_key": False,
            "nullable": True
        }
    ]

    def test_table_exists(self, db_inspector):
        assert db_inspector.has_table(self.__tablename__)

    def test_fields(self):
        for field in self.__fields__:
            field_attr = object.__getattribute__(self.__table__, field['name'])
            assert str(field_attr.type) == field['type']
            assert field_attr.primary_key == field['primary_key']
            assert field_attr.nullable == field['nullable']


class TestCustomerTable:

    __tablename__ = 'Customer'

    __table__ = Part_1.Customer

    __fields__ = [
        {
            "name": "customer_id",
            "type": "INTEGER",
            "primary_key": True,
            "nullable": False
        },
        {
            "name": "customer_name",
            "type": "VARCHAR(32)",
            "primary_key": False,
            "nullable": False
        },
        {
            "name": "customer_age",
            "type": "INTEGER",
            "primary_key": False,
            "nullable": True
        }
    ]

    def test_table_exists(self, db_inspector):
        assert db_inspector.has_table(self.__tablename__)

    def test_fields(self):
        for field in self.__fields__:
            field_attr = object.__getattribute__(self.__table__, field['name'])
            assert str(field_attr.type) == field['type']
            assert field_attr.primary_key == field['primary_key']
            assert field_attr.nullable == field['nullable']
