import tweepy
import csv
import pandas as pd


# keys and tokens from the Twitter Dev Console
consumer_key = 'FgCG8zcxF4oINeuAqUYzOw9xh'
consumer_secret = 'SrSu7WhrYUpMZnHw7a5ui92rUA1n2jXNoZVb3nJ5wEsXC5xlN9'
access_token = '975924102190874624-uk5zGlYRwItkj7pZO2m89NefRm5DFLg'
access_token_secret = 'ChvmTjG8hl61xUrXkk3AdKcXMlvAKf4ise1kIQLKsnPu4'

#Twitter only allows access to a users most recent 3240 tweets with this method

#authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#initialize a list to hold all the tweepy Tweets
alltweets = []    

#make initial request for most recent tweets (200 is the maximum allowed count)
new_tweets = api.search(q="#DonaldTrump",count=200,tweet_mode="extended")

#save most recent tweets
alltweets.extend(new_tweets)

#save the id of the oldest tweet less one
# oldest = alltweets[-1].id - 1
#keep grabbing tweets until there are no tweets left to grab
while len(new_tweets) > 0:
    # print "getting tweets before %s" % (oldest)

    #all subsiquent requests use the max_id param to prevent duplicates
    new_tweets = api.search(q="#DonaldTrump",count=200,tweet_mode="extended")

    #save most recent tweets
    alltweets.extend(new_tweets)

    #update the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # print "...%s tweets downloaded so far" % (len(alltweets))

#transform the tweepy tweets into a 2D array that will populate the csv    
outtweets = [[tweet.id_str, tweet.created_at, tweet.full_tweet.encode("utf-8"), tweet.retweet_count, tweet.favorite_count] for tweet in alltweets]

#write the csv    
with open('tweets.csv', 'w+') as f:
	writer = csv.writer(f)
	writer.writerow(["id","created_at","full_text","retweet_count","favorite_count"])
	writer.writerows(outtweets)

