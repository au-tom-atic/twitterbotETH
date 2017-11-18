#Import Twitter and Coinbase credentials

from credentials import *
import tweepy
import time 
from coinbase.wallet.client import Client

# Access and authorize Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Access coinbase
client = Client(api_key, api_secret)
price = client.get_spot_price(currency_pair = 'ETH-USD')

#Save String price as float
eth_price = price.amount
curr_eth_price = float(eth_price)
prev_eth_price = curr_eth_price
price_str = ('Current #ether value is: $%.2f #ethereum #crypto') % curr_eth_price
print(price_str)
api.update_status(price_str)

#wait an hour before checking agin
time.sleep(3600)

#run forever
while True:
	#get the new price
	price = client.get_spot_price(currency_pair = 'ETH-USD')
	eth_price = price.amount
	curr_eth_price = float(eth_price)
	
	if curr_eth_price == prev_eth_price:
		price_str = ('Current #ether value is: $%.2f #ethereum #crypto') % curr_eth_price
	elif curr_eth_price > prev_eth_price:
		diff = curr_eth_price - prev_eth_price
		price_str = ('Current #ether value is: $%.2f, increased by $%.2f #ethereum #crypto') % (curr_eth_price, diff)
	elif curr_eth_price < prev_eth_price:
		diff = curr_eth_price - prev_eth_price
		price_str = ('Current #ether value is: $%.2f, decreased by $%.2f #ethereum #crypto') % (curr_eth_price, diff)
	else:
		print('error!')
	
	api.update_status(price_str)
	print(price_str)
	#save the old price
	prev_eth_price = curr_eth_price
	#wait an hour
	time.sleep(3600)

print('The loop ended in some kinda error ')

