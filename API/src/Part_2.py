import tweepy
from tweepy import auth



def connect_api():
    """
    connect_api 함수는 tweepy 로 API 를 연결한 'api' 객체를 리턴합니다.

    Hint: api 객체는 tweepy.API 로 만들 수 있습니다.
    """

    api_key = 'Szsq4RvioNXSgN7dafcUtbKOT'
    api_key_secret = 't6yaPBEiZm8SLnJq8jWz3aso0aEnVMvI1gEqQ5GDetnreWY7n2'
    access_token = '1418126345083654148-3utXxpG6uY3Rp5hCWeK6pRJ0ZMxO1I'
    access_token_secret = 'cs31nhFzIBdeNtzoIjanRMgN6nOU0jKdBFvNCwEjIIYAQ'
    
    #api의 key와 secret 넣기
    auth = tweepy.OAuthHandler(api_key,api_key_secret)
    # acess의 token과 secret 넣기
    auth.set_access_token(access_token, access_token_secret)
    # 트위터 api
    api = tweepy.API(auth)

    return api

print(connect_api())


def get_tweets(api, username):
    """
    'username' 이 주어지면 해당 유저의 트윗들을 가지고 올 수 있어야 합니다.
    각 트윗은 140 자 이상이어도 모든 내용을 가지고 올 수 있어야 합니다.

    Hint: 'tweet_mode' 에 대해서 알아보세요!
    """
    # tweet_mode 에서 extended 적용 시 글자 수 많게 가능
    tweets = api.user_timeline(username, tweet_mode='extended')
    return tweets


