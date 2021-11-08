import tweepy

api_key = 'wG7fjjHRpjOpl4kzb2uBr2rPa'
api_secret = '8rZQusvG94uWomCNWbqu24iuvUADKHqLtRopLBsXrFwhUUV2Lb'

access_token = '1320589941349388289-Sy0NaTR46SNzTCDT5t0l0vwU1HKnh3'
access_secret = 'Xr1tSr3056lIVr8UZs2a69VJjrBUZH6gsur47VrzB5wxF'

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def get_user(screen_name):
    """
    `get_user` 함수는 트위터의 `screen_name` 이 주어지면 tweepy 를 통해 해당
    트위터 유저를 조회한 객체를 그대로 리턴합니다.
    """
    raw_user = None
    return raw_user

def get_tweets(screen_name):
    """
    `get_tweets` 함수는 트위터의 `screen_name` 이 주어지면 tweepy 를 통해 해당 트위터 유저의 트윗들을 조회한 리스트를 리턴합니다.
     - 리턴되는 트윗에는 리트윗 (retweet) 을 포함하지 않습니다.
     - 140 글자가 넘는 경우에도 다 가져올 수 있어야 합니다.
     - 답변 트윗 (retweet) 들은 포함하지 않습니다.
     - 한 페이지당 50 개의 트윗을 가져오도록 설정해야 합니다.

    Hint:

     - get_tweets 는 tweepy 의 user_timeline 함수를 사용합니다.
     - 다음 파라미터들을 어떻게 사용하는지 찾아보세요.
         - 'screeen_name'
         - 'tweet_mode'
         - 'include_rts'
         - 'count'
         - 'exclude_replies'
    """

    raw_tweets = None
    
    return raw_tweets
