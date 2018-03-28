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
csvFile = open('tweets.csv', 'w+')
# Use csv Writer
csvWriter = csv.writer(csvFile)
tag = "#TuesdayThoughts"
limit = 0
csvWriter.writerow(["ID", "Username", "Twitter @", "Tweet","Tweeted At", "Favourite Count", "Retweet Count"])
csvWriter.writerow([])

for tweet in tweepy.Cursor(api.search,q=""+tag,count=350,lang="en",tweet_mode = "extended").items():
    # print (tweet.created_at, tweet.text)
    temp = tweet.full_text
    if temp.startswith('RT @'):
    	continue
    print ("ID:", tweet.id)
    print ("User ID:", tweet.user.id)
    print ("Name: ", tweet.user.name)
    print ("Twitter @:", tweet.user.screen_name)
    print ("Text:", tweet.full_text)
    print ("Tweet length:", len(tweet.full_text))
    print ("Created:", tweet.created_at)
    print ("Favorite Count:", tweet.favorite_count)
    print ("Retweet count:", tweet.retweet_count)
    # print ("Retweeted? :", tweet.retweeted)
    # print ("Truncated:", tweet.truncated)
    print ("\n\n")

    csvWriter.writerow([tweet.id, tweet.user.name, tweet.user.screen_name, tweet.full_text,tweet.created_at, tweet.favorite_count, tweet.retweet_count])
    csvWriter.writerow([])
    limit = limit + 1
    if limit == 10:
    	break

print ("Done")
# print ("\nTweets -")
# print (tweets)

# convert 'tweets' list to pandas.DataFrame
# tweets_df = pd.DataFrame(vars(tweets[i]) for i in range(len(tweets)))

# # define attributes you want
# tweet_atts = [
# 'id', 'text', 'created_at', 'geo', 'coordinates','favorite_count',
# 'retweet_count', 'source'
# ]

# # subset dataframe
# tweets_df = tweets_df[tweet_atts]


# # define file path (string) to save csv file to
# FILE_PATH = "ua.csv"

# # use pandas to save dataframe to csv
# tweets_df.to_csv(FILE_PATH)


