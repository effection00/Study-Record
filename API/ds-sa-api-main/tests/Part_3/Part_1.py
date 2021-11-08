# from sqlalchemy.orm import RelationshipProperty, sessionmaker
# from sqlalchemy.sql import sqltypes
# from src.Part_3 import (User, Tweet, init_database, add_tweet, add_user,
                        # delete_tweet, delete_user)


# def test_init_database(test_engine):
    # assert test_engine.table_names().__len__() == 0
    # init_database(test_engine)
    # assert test_engine.table_names().__len__() == 2


# def test_tweet_table():
    # assert Tweet.__tablename__ == 'tweet'


# def test_tweet_table_column_id():
    # assert Tweet.id.primary_key is True
    # assert isinstance(Tweet.id.type, sqltypes.Integer)


# def test_tweet_table_column_full_text():
    # assert isinstance(Tweet.full_text.type, sqltypes.String)


# def test_tweet_table_column_user_id():
    # expected_ans = "{ForeignKey('user.id')}"
    # assert isinstance(Tweet.user_id.type, sqltypes.Integer)
    # assert Tweet.__table__.foreign_keys.__str__() == expected_ans


# def test_user_table():
    # assert User.__tablename__ == 'user'


# def test_user_table_column_id():
    # assert User.id.primary_key is True
    # assert isinstance(User.id.type, sqltypes.Integer)


# def test_user_table_column_screen_name():
    # assert isinstance(User.screen_name.type, sqltypes.String)


# def test_user_table_column_tweets():
    # assert isinstance(User.tweets.property, RelationshipProperty)


# def test_add_single_tweet(test_session):
    # session = test_session

    # assert session.query(Tweet).all().__len__() == 0

    # add_tweet('patrick', 'under the sea', session)

    # assert session.query(Tweet).all().__len__() == 1


# def test_add_single_user(test_session):
    # session = test_session

    # assert session.query(User).all().__len__() == 0

    # add_user('spongebob', session)

    # assert session.query(User).all().__len__() == 1


# def test_delete_tweet(test_session):
    # session = test_session

    # new_tweet = Tweet(full_text='welcome to seaworld', user_id=1)
    # session.add(new_tweet)

    # assert session.query(Tweet).all().__len__() == 1

    # delete_tweet(1, session)
    # assert session.query(Tweet).all().__len__() == 0


# def test_delete_user(test_session):
    # session = test_session

    # session.add(User(screen_name='Darcy'))
    # assert session.query(User).all().__len__() == 1

    # delete_user(1, session)
    # assert session.query(User).all().__len__() == 0
