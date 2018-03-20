import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'FgCG8zcxF4oINeuAqUYzOw9xh'
consumer_secret = 'SrSu7WhrYUpMZnHw7a5ui92rUA1n2jXNoZVb3nJ5wEsXC5xlN9'
access_token = '975924102190874624-uk5zGlYRwItkj7pZO2m89NefRm5DFLg'
access_token_secret = 'ChvmTjG8hl61xUrXkk3AdKcXMlvAKf4ise1kIQLKsnPu4'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
# csvFile = open('ua.csv', 'w+')
# Use csv Writer
# csvWriter = csv.writer(csvFile)
tag = "#TuesdayThoughts"
limit = 0
tweets = []

for tweet in tweepy.Cursor(api.search,q=""+tag,count=100,lang="en",since="2017-04-03").items():
    print (tweet.created_at, tweet.text)
    # csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    tweets.append(tweet)
    limit = limit + 1
    if limit == 10:
    	break

print ("Done")
# print ("\nTweets -")
# print (tweets)

# convert 'tweets' list to pandas.DataFrame
tweets_df = pd.DataFrame(vars(tweets[i]) for i in range(len(tweets)))

# define attributes you want
tweet_atts = [
'id', 'text', 'created_at', 'favorite_count',
'retweet_count', 'source'
]

# subset dataframe
# tweets_df = tweets_df[tweet_atts]


# define file path (string) to save csv file to
FILE_PATH = "res.csv"

# use pandas to save dataframe to csv
tweets_df.to_csv(FILE_PATH)


