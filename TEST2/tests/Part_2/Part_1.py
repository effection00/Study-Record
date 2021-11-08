from src import Part_2


class TestAnimalTable:

    __tablename__ = 'Animals'

    __table__ = Part_2.Animal

    __fields__ = [
        {
            "name": "id",
            "type": "INTEGER",
            "primary_key": True,
            "nullable": False
        },
        {
            "name": "name",
            "type": "VARCHAR(32)",
            "primary_key": False,
            "nullable": False
        },
        {
            "name": "age",
            "type": "INTEGER",
            "primary_key": False,
            "nullable": True
        }
    ]

    def test_table_exists(self, db_inspector):
        try:
            assert db_inspector.has_table(self.__tablename__)
        except AttributeError as e:
            assert 'Animals' in db_inspector.get_table_names()

    def test_fields(self):
        for field in self.__fields__:
            field_attr = object.__getattribute__(self.__table__, field['name'])
            assert str(field_attr.type) == field['type']
            assert field_attr.primary_key == field['primary_key']
            assert field_attr.nullable == field['nullable']
