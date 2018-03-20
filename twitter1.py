from Twython import Twython

TWITTER_APP_KEY = 'xxxxx' #supply the appropriate value
TWITTER_APP_KEY_SECRET = 'xxxxx' 
TWITTER_ACCESS_TOKEN = 'xxxxxx'
TWITTER_ACCESS_TOKEN_SECRET = 'xxxxx'

t = Twython(app_key=TWITTER_APP_KEY, 
            app_secret=TWITTER_APP_KEY_SECRET, 
            oauth_token=TWITTER_ACCESS_TOKEN, 
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

search = t.search(q='#omg',   #**supply whatever query you want here**
                  count=100)

tweets = search['statuses']

for tweet in tweets:
  print tweet['id_str'], '\n', tweet['text'], '\n\n\n'