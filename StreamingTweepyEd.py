from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

CONSUMER_KEY = '<Put API key Here>'
CONSUMER_SECRET ='<Put API secret Here>'
OAUTH_TOKEN = '<Put Access token Here>'
OAUTH_TOKEN_SECRET = '<Put Access token secret Here>'


class listener(StreamListener):

	def on_data(self, data):
		try:
			print data
			saveFile = open('Education.txt', 'a')
			saveFile.write(data)
			saveFile.write('\n')
			saveFile.close()
			return True
		except BaseException, e:
			print 'failed ondata,',str(e)
			time.sleep(5)

	def on_error(self, status):
		print status

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twitterStream = Stream(auth, listener())

twitterStream.filter(track=["#education", "#educationaltechnology", "#educationforall", "@Ed4Excellence", "@usedgov"])
