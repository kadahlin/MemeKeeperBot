"""
Kyle Dahlin 2017
The Twitter Agent class is used to create a container for connecting to 
Tweepy api and automating the calls to the main account.

"""

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
		"""
		Format and post the data in the title parameter in addition to 
		the image from the default output file defined in the Image 
		Maker class
		"""
		first = _get_line_from_file(FIRST_FILE)
		second = _get_line_from_file(SECOND_FILE)
		title = title[0].upper() + title[1:]
		title = title.replace("-", " ")

		self.api.update_with_media(OUTPUT_FILE, 
			first.replace(TITLE_PLACEHOLDER, title) + " " + second)
		

	def _get_line_from_file(self, filename):
		"""Get a random line from one of the phrases file."""
		with open(filename) as f:
			phrases = f.readlines()
			selection = phrases[randrange(len(phrases))]
			return selection.strip()

if __name__ == '__main__':
	"""Test for creating and formatting the status update"""
	t = TwitterAgent()
	title  = "test-meme-title"
	title = title[0].upper() + title[1:]
	title = title.replace("-", " ")
	print(t._get_line_from_file(FIRST_FILE).replace("[]", title) 
		+ " " + t._get_line_from_file(SECOND_FILE))

		



