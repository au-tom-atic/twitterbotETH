import tweepy
from time import sleep
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='#ethereum').items():
	try:
		print('/nTweet by @' + tweet.user.screen_name)
		
		if not tweet.user.following:
			tweet.user.follow()
			print('Follwed the user')
		
		sleep(300)

	except tweepy.TweepError as e:
		print(e.reason)

	except StopIteration:
		break
