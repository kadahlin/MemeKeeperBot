#Kyle Dahlin 2017

import time

class Logger:

	def __init__(self, filepath):
		self.filepath = filepath

	def log(self, message):
		with open(self.filepath, "a") as f:
			message = time.strftime("%d/%m/%Y | %H:%M -> ") + message
			f.write(message + '\n')

if __name__ == '__main__':
	l = Logger("debug.txt")
	l.log("first test")