import tweepy
import csv
# import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

def mining(tag, count=10):
	####input your credentials here
	consumer_key = 'FgCG8zcxF4oINeuAqUYzOw9xh'
	consumer_secret = 'SrSu7WhrYUpMZnHw7a5ui92rUA1n2jXNoZVb3nJ5wEsXC5xlN9'
	access_token = '975924102190874624-uk5zGlYRwItkj7pZO2m89NefRm5DFLg'
	access_token_secret = 'ChvmTjG8hl61xUrXkk3AdKcXMlvAKf4ise1kIQLKsnPu4'

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth,wait_on_rate_limit=True)

	# Open/Create a file to append data
	csvFile = open('tweets.csv', 'w+')
	# Use csv Writer
	csvWriter = csv.writer(csvFile)
	# tag = "#DonaldTrump"
	limit = 0
	res = ""
	positive = 0
	negative = 0
	neutral = 0
	csvWriter.writerow(["ID", "Username", "Twitter @", "Tweet","Tweeted At", "Favourite Count", "Retweet Count", "Sentiment"])
	csvWriter.writerow([])

	for tweet in tweepy.Cursor(api.search,q=""+tag,count=350,lang="en",tweet_mode = "extended").items():
	    # print (tweet.created_at, tweet.text)
	    temp = tweet.full_text
	    if temp.startswith('RT @'):
	    	continue
	    blob = TextBlob(tweet.full_text)
	    if blob.sentiment.polarity > 0:
	        res = "Positive"
	        positive = positive+1
	    elif blob.sentiment.polarity == 0:
	        res = "Neutral"
	        neutral = neutral+1
	    else:
	        res = "Negative"
	        negative = negative+1


	    print ("ID:", tweet.id)
	    print ("User ID:", tweet.user.id)
	    print ("Name: ", tweet.user.name)
	    print ("Twitter @:", tweet.user.screen_name)
	    print ("Text:", tweet.full_text)
	    print ("Tweet length:", len(tweet.full_text))
	    print ("Created:(UTC)", tweet.created_at)
	    print ("Favorite Count:", tweet.favorite_count)
	    print ("Retweet count:", tweet.retweet_count)
	    print ("Sentiment:", res)
	    # print ("Retweeted? :", tweet.retweeted)
	    # print ("Truncated:", tweet.truncated)
	    print ("\n\n")
	    
	    csvWriter.writerow([tweet.id, tweet.user.name, tweet.user.screen_name, tweet.full_text,tweet.created_at, tweet.favorite_count, tweet.retweet_count, res])
	    csvWriter.writerow([])
	    limit = limit + 1
	    if limit == int(count):
	    	break

	print ("Done")

	print ("\n\n\n")
	total = positive+negative+neutral
	positivePercent = 100*(positive/total)
	negativePercent = 100*(negative/total)
	neutralPercent = 100*(neutral/total)

	print ("Positive tweets: {} %".format(positivePercent))
	print ("Negative tweets: {} %".format(negativePercent))
	print ("Neutral tweets: {} %".format(neutralPercent))

	ret_list = []
	ret_list.append(str(positivePercent))
	ret_list.append(str(negativePercent))
	ret_list.append(str(neutralPercent))

	return ret_list

	# infile = 'tweets.csv'

	# with open(infile, 'r') as csvfile:
	#     rows = csv.reader(csvfile)
	#     for row in rows:
	#         sentence = row[3]
	#         blob = TextBlob(sentence)
	#         print (blob.sentiment)


	labels = 'Neutral', 'Positive', 'Negative'
	sizes = []
	sizes.append(neutralPercent)
	sizes.append(positivePercent)
	sizes.append(negativePercent)
	colors = ['lightskyblue','yellowgreen', 'lightcoral']
	explode = (0, 0, 0)  # explode 1st slice
	 
	# Plot
	plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
	plt.suptitle("Sentiment Analysis of {} tweets related to {}".format(limit, tag))
	plt.axis('equal')
	plt.show()

