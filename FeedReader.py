"""
Kyle Dahlin 2017

The FeedReader class is used to read the data from the rss feed of the 
website. The data to post method will do two main things
1. Return true or false is there is potential data to send to the 
	Twitter Agent
2. Save the title of the meme to post inside the self.title field to 
	be referenced from the class that holds the FeedReader ( in this case
	the Runner class)
"""

import urllib.request
import xml.etree.ElementTree as ET
import re

RSS_LINK = "http://knowyourmeme.com/newsfeed.rss"

class FeedReader:


	def __init__(self):
		self.title = ""


	"""Get a list of all the posts in the RSS feed that are marked as /memes/"""
	def _get_url_data(self):
		connection = urllib.request.urlopen(RSS_LINK)
		file_contents = connection.read().decode('utf-8')

		root = ET.fromstring(file_contents)
		channel = root.find('channel')
		tuples = []

		for item in channel.findall('item'):
			if item.find('link') == None:
				continue
			if "/memes/" not in item.find('link').text:
				continue

			title = item.find('link').text
			title =  re.search(r'memes/.*', title).group(0)[6:]
			if "/" in title:
				continue

			image_url = item.find('description').text
			image_url = re.search(r'src=\"([A-Za-z0-9:_\./\\-]*)\"', image_url).group(0)[5:-1]

			tuples.append((title, image_url))
		return tuples


	"""Save the image at the supplied url to the local file that will be posted"""
	def _save_image(self, url):
		image_file = urllib.request.urlopen(url).read()

		with open(self.title + ".jpg", "wb") as f:
			f.write(image_file)


	"""Get a list of titles that have already been posted and saved"""
	def _get_obit_data(self):
		file_contents = ""
		with open("obituary.txt") as file:
			file_contents = file.readlines()
		return [line.strip() for line in file_contents]


	"""Save the title to the obit file of already dead memes"""
	def _write_to_obit(self, name):
		with open("obituary.txt", "a") as f:
			f.write(name + '\n')


	"""Called by the runner and will return true if there is data to post and 
	false otherwise"""
	def data_to_post(self):
		data = self._get_url_data()
		file_contents = self._get_obit_data()
		print(file_contents)
		for tuple_items in data:
			if(tuple_items[0] not in file_contents):
				self.title = tuple_items[0]
				self._write_to_obit(tuple_items[0])
				self._save_image(tuple_items[1])
				return True;
		return false





		




