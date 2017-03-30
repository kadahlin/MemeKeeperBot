"""
Kyle Dahlin 2017

The Logger class will format logs as the bot posts and fetches data. The
log object is initialized with a file name to post all of the logs to. In the 
future the logger will output more detailed log messages to stdout.
"""

import time

class Logger:

	def __init__(self, filepath):
		"""Remember the file path"""
		self.filepath = filepath

	def log(self, message):
		"""Write the message to the default filepath saved in the object"""
		with open(self.filepath, "a") as f:
			message = time.strftime("%d/%m/%Y | %H:%M -> ") + message
			f.write(message + '\n')

if __name__ == '__main__':
	l = Logger("debug.txt")
	l.log("test log entry")