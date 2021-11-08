import os
import pytest
from sqlalchemy import inspect, create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from src.Part_2 import Base

pytest.TEST_DB_FILEPATH = 'tests/test.db'


@pytest.fixture(scope="session")
def db_engine():
    engine_ = create_engine(f"sqlite:///{pytest.TEST_DB_FILEPATH}", echo=True)
    yield engine_
    engine_.dispose()
    os.remove(pytest.TEST_DB_FILEPATH)


@pytest.fixture(scope='module')
def db_session_factory(db_engine):
    return scoped_session(sessionmaker(bind=db_engine))


@pytest.fixture(scope='function')
def db_session(db_session_factory):
    session_ = db_session_factory()
    yield session_
    session_.rollback()
    session_.close()


@pytest.fixture(scope='function')
def db_inspector(db_engine):
    return inspect(db_engine)


@pytest.fixture(autouse=True, scope="function")
def config_db(db_engine):
    Base.metadata.drop_all(bind=db_engine)
    Base.metadata.create_all(bind=db_engine)
    yield
