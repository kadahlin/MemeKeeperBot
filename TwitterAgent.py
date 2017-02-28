#Class to pull the data from the Runner and use tweepy to post to the 
#main account

import tweepy
from keys import *
from random import randrange
from ImageMaker import OUTPUT_FILE

SECOND_FILE = "second.txt"
FIRST_FILE = "first.txt"
TITLE_PLACEHOLDER = "[]"

class TwitterAgent:
	"""Autoamte the postings to the twitter account"""

	def __init__(self):
		self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		self.auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

		self.api = tweepy.API(self.auth)

	def post_data(self, title):
		first = _get_line_from_file(FIRST_FILE)
		second = _get_line_from_file(SECOND_FILE)
		title = title[0].upper() + title[1:]
		title = title.replace("-", " ")

		self.api.update_with_media(OUTPUT_FILE, 
			first.replace(TITLE_PLACEHOLDER, title) + " " + second)
		

	def _get_line_from_file(self, filename):
		with open(filename) as f:
			phrases = f.readlines()
			selection = phrases[randrange(len(phrases))]
			return selection.strip()

if __name__ == '__main__':
	t = TwitterAgent()
	title  = "test-meme-title"
	title = title[0].upper() + title[1:]
	title = title.replace("-", " ")
	print(t._get_line_from_file(FIRST_FILE).replace("[]", title) 
		+ " " + t._get_line_from_file(SECOND_FILE))

		



