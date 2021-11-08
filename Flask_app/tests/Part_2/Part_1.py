import pytest
from tweepy.error import TweepError
from twit_app.services import tweepy_api

# testing services
def test_tweepy_connection():
    api = tweepy_api.api

    try:
        assert api.verify_credentials() is not False
    except TweepError as e:
        pytest.fail('Tweepy 인증이 실패했습니다. \nAPI 인증 정보를 확인해주세요.')
        print(e)


def test_tweepy_get_user():
    api = tweepy_api.api

    test_user = {
        'screen_name':'bts_bighit',
        'name':'BTS_official'
    }

    raw_user = tweepy_api.get_user(test_user['screen_name'])

    assert raw_user.name == test_user['name']


def test_tweepy_get_tweets():
    api = tweepy_api.api

    test_user = {
        'screen_name':'bts_bighit',
        'name':'BTS_official'
    }

    raw_tweets = tweepy_api.get_tweets(test_user['screen_name'])

    assert len(raw_tweets) != 0

