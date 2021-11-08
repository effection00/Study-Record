import os
import pytest
import pickle
import shutil
import sqlite3
from string import Template

pytest.RESOURCE_PATH = os.path.join(os.getcwd(), 'tests', 'resources')


@pytest.fixture(scope="module")
def test_db_session():
    DB_FILENAME = 'chinook.db'
    DB_FILEPATH = os.path.join(os.getcwd(), DB_FILENAME)
    TESTDB_FILEPATH = os.path.join(os.path.dirname(__file__), 'test.db')

    shutil.copy(DB_FILEPATH, TESTDB_FILEPATH, follow_symlinks=True)

    if not os.path.isfile(DB_FILEPATH):
        print(f'{DB_FILENAME} not found')
        return

    conn = sqlite3.connect(TESTDB_FILEPATH)
    yield conn
    conn.close()
    os.remove(TESTDB_FILEPATH)
@pytest.fixture(autouse=True, scope="module")
def setup_teardown_msg():
    template = Template("""
        -------------------------------------
        $msg...
        -------------------------------------
        """)
    yield print(template.substitute(msg="Setting up"))
    print(template.substitute(msg="Tearing down"))


@pytest.fixture(autouse=True, scope="session")
def pkl_opener():
    def returner(file_path):
        with open(file_path, 'rb') as f:
            content = pickle.load(f)
        return content
    pytest.pkl_opener = returner
