import sys
import numpy
from PIL import Image

script,filename = sys.argv

words = open(filename).read().split() # splits the random numbers in the file to list
words = words*6 # To get 49152 numbers so that i could build 128X128 pixel array
list_tuple = []

for i in range(0,len(words),3):
    list_tuple.append(tuple(words[i:i+3]))#converts the number in list to tuples of 3

list_rgb=[]
for i in range(0,len(l),128):
    list_rgb.append(list(l[i:i+128]))#converts the list of tuple to 128X128 pixel array

imarray = numpy.array(list_rgb)
im = Image.fromarray(imarray.astype('uint8')).convert('RGBA')
im.save('result_image.bmp')#saves the generated image in bitmap format
