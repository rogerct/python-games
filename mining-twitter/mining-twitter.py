import tweepy
from tweepy import OAuthHandler

consumer_key = 'KsAzHOKi1TlOz3fb2cnOmMpbg'
consumer_secret = 'DB34RubkMIt3JYOzhxoHdLfGvocZ3dhN2OKVs0hlO49dxMKSjG'
access_token = '1165402470-OcLrtL1WORR5K9hiXRAZ74JTPczBVWCAgBEM8LY '
access_secret = 'bcFH2viZFileJPXhmy0WW1lXVhBEa4MNEkw86GMLxC7nU'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


#Read our timeline
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)


#list of followers

for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend._json)


#list of tweets

for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)
