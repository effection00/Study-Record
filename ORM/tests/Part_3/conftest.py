# import os
# import pytest
# from sqlalchemy import create_engine, inspect
# from sqlalchemy.orm import scoped_session, sessionmaker
# from src.Part_3 import Base, DATABASE_URI


# @pytest.fixture(scope="session")
# def part3_engine():
#     engine_ = create_engine(DATABASE_URI, echo=True)
#     yield engine_
#     engine_.dispose()


# @pytest.fixture(scope='module')
# def part3_session_factory(part3_engine):
#     return scoped_session(sessionmaker(bind=part3_engine))


# @pytest.fixture(scope='function')
# def part3_session(part3_session_factory):
#     session_ = part3_session_factory()
#     yield session_
#     session_.rollback()
#     session_.close()


# @pytest.fixture(scope='function')
# def part3_db_inspector(part3_engine):
#     return inspect(part3_engine)
