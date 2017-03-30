#Kyle Dahlin 2017

from PIL import Image

BACKGROUND_FILE = "dampe.png" #tentative
OUTPUT_FILE = "test.png"

PASTE_HEIGHT = 150
PASTE_WIDTH = 250

class ImageMaker:

	def make_image(self, title):
		"""Create the new shopped image. This is assume there is a file in the current 
		directory that is named title + ".jpg". It will create a new image that is the assumed 
		image scaled down and placed inside of the main grave keeper image. 
		"""
		background = Image.open(BACKGROUND_FILE).copy()
		foreground = Image.open(title + ".jpg").copy().resize((PASTE_WIDTH, PASTE_HEIGHT))
		background.paste(foreground, (60,415))
		background.save(OUTPUT_FILE)
		


if __name__ == "__main__":
	i = ImageMaker()
	i.make_image("test-image")
