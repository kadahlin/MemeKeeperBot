#Kyle Dahlin 2017 - Meme grave keeper

"""
Main file for the entire program. Reads from RSS feed of Know your 
meme.com and posts from the most recent article that is not already 
saved in the file "obituary.txt". The twitter keys are for the account 
with the username "wherememesdie". The script reads the data, stores 
the data, posts the data and then sleeps for 24 hours and repeats.
"""

from FeedReader import FeedReader
from TwitterAgent import TwitterAgent
from ImageMaker import ImageMaker
from Logger import Logger

import time
import sys
from threading import Thread

class Runner:
	
	def __init__(self):	
		"""Create and combine all of the pieces together"""
		self.twitter_agent = TwitterAgent()
		self.feed_reader = FeedReader()
		self.image_maker = ImageMaker()
		self.logger = Logger("log.txt")
		

	def run(self):
		"""Start the loop and make calls to the controlling agents"""
		try:
			while True:
				if(self.feed_reader.data_to_post()):
					self.image_maker.make_image(self.feed_reader.title)
					self.twitter_agent.post_data(self.feed_reader.title)
					self.logger.log("automated post")
				time.sleep(86164)
		except KeyboardInterrupt:
			print("I hope the execution went well Kyle :)")



if __name__ == '__main__':
	r = Runner()
	r.run()