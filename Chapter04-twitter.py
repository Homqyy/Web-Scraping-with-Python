from pythonScraping import *
from twitter import OAuth, Twitter, TwitterHTTPError

secretsData = getSecrets('twitter')

accessToken = secretsData['access_token']
accessTokenSecret = secretsData['access_token_secret']
apiKey = secretsData['api_key']
apiKeySecret = secretsData['api_key_secret']
bearerToken = secretsData['bearer_token']

t = Twitter(auth=OAuth(
    accessToken, accessTokenSecret, apiKey, apiKeySecret
))

try:
    publicTweets = t.statuses.home_timeline(count=10) 

    # 打印推文内容
    for tweet in publicTweets:
        print(tweet['text'])
except TwitterHTTPError as e:
    print(e)
