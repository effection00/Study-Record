# import pytest
# from pymongo import MongoClient
# from src.Part_4 import MONGO_URI, database_name, collection_name


# @pytest.fixture(scope='module')
# def connection():
    # conn = MongoClient(MONGO_URI)
    # yield conn
    # conn.close()


# @pytest.fixture
# def database_conn(connection):
    # database = connection[f"{database_name}"]
    # yield database


# @pytest.fixture
# def collection(database_conn):
    # collection = database_conn[f"{collection_name}"]
    # yield collection
