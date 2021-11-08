# import pickle
# import psycopg2
# import pytest
# from src import Part_3

# @pytest.fixture(autouse=True, scope="session")
# def pkl_opener():
    # def returner(file_path):
        # with open(file_path, 'rb') as f:
            # content = pickle.load(f)
        # return content
    # pytest.pkl_opener = returner

# @pytest.fixture(scope="module")
# def db_connection():
    # conn = psycopg2.connect(
        # host=Part_3.host,
        # user=Part_3.user,
        # password=Part_3.password,
        # database=Part_3.database
    # )
    # yield conn
    # conn.close()


# @pytest.fixture(scope="function")
# def cursor(db_connection):
    # cursor = db_connection.cursor()
    # pytest.cur = cursor
    # yield cursor
    # cursor.close()
