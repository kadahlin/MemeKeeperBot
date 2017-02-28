#Kyle Dahlin 2017 - Meme grave keeper

from FeedReader import FeedReader
from TwitterAgent import TwitterAgent
from ImageMaker import ImageMaker
from Logger import Logger

import time
import sys
from threading import Thread

class Runner:
	
	def __init__(self):	
		"""The brain of the script"""
		self.twitter_agent = TwitterAgent()
		self.feed_reader = FeedReader()
		self.image_maker = ImageMaker()
		self.logger = Logger("log.txt")
		

	def run(self):
		"""start the loops and make calls to the controlling agents"""
		try:
			while True:
				if(self.feed_reader.data_to_post()):
					self.image_maker.make_image(self.feed_reader.title)
					#self.twitter_agent.post_data(self.feed_reader.title)
					self.logger.log("automated post")
				time.sleep(86164)
		except KeyboardInterrupt:
			print("I hope the execution went well Kyle :)")



if __name__ == '__main__':
	r = Runner()
	r.run()