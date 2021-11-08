import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
try:
    from src.Part_3 import init_database
except ImportError as e:
    print('해당 테스트 파일을 실행하기 위해서는 주석들을 풀어주세요')


DATABASE_URI = "sqlite+pysqlite:///:memory:"

@pytest.fixture
def test_engine():
    engine = create_engine(DATABASE_URI)

    return engine


@pytest.fixture
def test_session():
    engine = create_engine(DATABASE_URI)
    init_database(engine)
    session = sessionmaker(engine)()
    yield session
    session.close()
