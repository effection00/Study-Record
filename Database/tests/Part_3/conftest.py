import pytest


@pytest.fixture(autouse=True, scope="function")
def cursor(test_db_session):
    pytest.cur = test_db_session.cursor()
    yield
    pytest.cur.close()
