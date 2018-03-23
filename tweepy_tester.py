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
csvFile = open('ua.csv', 'w+')
# Use csv Writer
csvWriter = csv.writer(csvFile)
tag = "#FridayFeeling"
limit = 0
csvWriter.writerow(["ID", "Username", "Twitter @", "Tweet","Tweeted At", "Favourite Count", "Retweet Count"])

for tweet in tweepy.Cursor(api.search,q=""+tag,count=300,lang="en",since="2017-04-03").items():
    # print (tweet.created_at, tweet.text)
    if tweet.truncated == "True":
    	continue
    print ("ID:", tweet.id)
    print ("User ID:", tweet.user.id)
    print ("Name: ", tweet.user.name)
    print ("Twitter @:", tweet.user.screen_name)
    print ("Text:", tweet.text)
    print ("Created:", tweet.created_at)
    print ("Favorite Count:", tweet.favorite_count)
    print ("Retweet count:", tweet.retweet_count)
    # print ("Truncated:", tweet.truncated)
    print ("\n\n")

    csvWriter.writerow([tweet.id, tweet.user.name, tweet.user.screen_name, tweet.text,tweet.created_at, tweet.favorite_count, tweet.retweet_count])
    csvWriter.writerow([])
    limit = limit + 1
    if limit == 5:
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


