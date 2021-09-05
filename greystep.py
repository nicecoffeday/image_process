from PIL import Image
import os

image_file = Image.open("pumpkin.png") # open colour image
image_file = image_file.convert('L') # convert image to black and white
image_file.save('result.png')
		

for file in os.listdir('.'): #列出所在位置中 檔案的檔名
	print(file)