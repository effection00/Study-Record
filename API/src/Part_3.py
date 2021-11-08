from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relation, sessionmaker, relationship
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.functions import user

DATABASE_URI = "sqlite+pysqlite:///twitter_db.sqlite3"
engine = create_engine(DATABASE_URI)
Base = declarative_base()


Session = sessionmaker(bind=engine)
session = Session()

class User(Base):

    """
    User 테이블을 완성합니다.

    요구사항:
        - 테이블 이름이 'user' 이어야 합니다.
        - id, screen_name, tweets 칼럼들이 있어야 합니다.
    """

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    screen_name = Column(String)

    def __repr__(self):
        return f"User({self.id!r})"
    
    tweets = relationship('Tweet', back_populates='users') 


class Tweet(Base):
    """
    Tweet 테이블을 완성합니다.

    요구사항:
        - 테이블 이름이 'tweet' 이어야 합니다.
        - id, full_text, user_id 칼럼들이 있어야 합니다.
    """

    __tablename__ = 'tweet'

    id = Column(Integer,primary_key=True)
    full_text = Column(String)
    user_id = Column(Integer,  ForeignKey(User.id))

    def __repr__(self):
        return f"Tweet({self.id!r})"
    users = relationship('User', back_populates='tweets') 

# create_engine을 통해 해당 db로 접속 가능하게 engine 생성
def init_database(engine=engine):
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    """
    init_database 함수는 데이터베이스를 리셋합니다. 기존 테이블들을 제거하고
    새로 생성해야 합니다.

    파라미터:
        - engine: 데이터베이스 엔진입니다. 기본값은 Part_2.py 에 있는 engine
        객체입니다.

    리턴:
        - 별도로 없습니다.
    """

    pass


def add_tweet(username, tweet_text, session=session):
    find_user = session.query(User).filter(User.screen_name == username).first()
    
    if find_user is None:
        add_user(username)
        p_tweet = Tweet(full_text=tweet_text, user_id= add_user(username).id)

    session.add(p_tweet)
    session.commit()


    """
    add_tweet 함수는 tweet_text 와 username 이 주어지면 해당 유저와 연결된
    새로운 트윗을 추가합니다.

    만약에 존재하지 않은 유저라면 해당 유저를 추가한 뒤에 트윗을 삽입합니다.

    파라미터:
        - username: 추가할 유저 이름을 담은 문자열(str) 입니다.
        - tweet_text: 추가할 트윗을 담은 문자열(str) 입니다.
        - session: 트윗을 어디에 추가할지 알려주는 세션 객체입니다.

    리턴:
        - tweet 객체: 데이터베이스에 새로 추가한 tweet 클래스 인스턴스를
        리턴합니다.
    """
    return p_tweet


def add_user(username, session=session):
    """
    add_user 함수는 user 를 새로 추가하고 해당 user 객체를 리턴합니다. 만약에
    username 을 가지고 있는 유저가 기존에 존재한다면 해당 유저를 리턴합니다.

    파라미터:
        - username: 추가할 유저 이름을 담은 문자열(str) 입니다.
        - session: 유저를 어디에 추가할지 알려주는 세션 객체입니다.

    리턴:
        - user 객체: 데이터베이스에 새로 추가한 user 클래스 인스턴스를
        리턴합니다.
    """

    p_user = session.query(User).filter(User.screen_name == username).first()

    if p_user != None:
        return p_user
    else:
        p_user = User(screen_name=username)
        session.add(p_user)
        session.commit()
        return p_user


def delete_tweet(tweet_id, session=session):
    """
    delete_tweet 함수는 tweet_id 가 주어지면 해당 트윗 데이터베이스에서 삭제해야 합니다.

    파라미터:
        - tweet_id: 데이터베이스에서 삭제할 트윗 레코드 고유번호(int) 입니다.
        - session: 트윗 레코드를 어느 데이터베이스에서 제거해야 할지 알려주는
        세션 객체입니다.

    리턴:
        - 별도로 없습니다.
    """

    tweet = (
        session.query(Tweet)
        .filter(Tweet.id == tweet_id)
        .one_or_none()
    )

    if tweet is None:
        return "Tweet does not exist"

    session.delete(tweet)
    session.commit()

    return f"Tweet ({tweet_id}) deleted"


def delete_user(user_id, session=session):
    """
    delete_user 함수는 user_id 가 주어지면 데이터베이스에서 해당 user 를 삭제하고
    user 와 연관된 연관된 트윗들도 같이 삭제해야 합니다.

    파라미터:
        - user_id: 데이터베이스에서 삭제할 트윗 레코드 고유번호(int) 입니다.
        - session: 유저 레코드를 어느 데이터베이스에서 제거해야 할지 알려주는
        세션 객체입니다.

    리턴:
        - 별도로 없습니다.
    """
    user = session.query(User).filter(User.id == user_id).first()
 
    if user is None:
        return 'there is no exist userid'



    delete_tweet(user_id)
    session.delete(user)
    
    session.commit()
    
    return f"User ({user_id}) deleted"



