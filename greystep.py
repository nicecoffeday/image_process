from PIL import Image
import os


for file in os.listdir('orig'): #列出所在位置中 檔案的檔名
    if file.endswith('.jpg'):
        image_file = Image.open('orig/' + file) # open colour image, add path orig/
        image_file = image_file.convert('L') # convert image to black and white
        image_file.save('result/' + file[:-4] + '_grey.png')

