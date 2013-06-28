#!/usr/bin/env python

from PIL import Image
import os
import sys
import shutil
from PIL import ImageOps

#portrait dimensions default 160x228
width = 160
height = 228
#offset to align source image. default is 55x14
imgOffset = 55,14

if not os.path.exists("source/"):
	print "Source folder not found. Created new folder. Please add source images to the source folder"
	os.mkdir("source/")
	sys.exit(3)
if not os.path.exists("output/"):
	os.mkdir("output/")
if not os.path.exists("used/"):
	os.mkdir("used/")
imgBG=Image.open("data/bg.png")
imgTop=Image.open("data/top.png")
numFiles=0
for file in os.listdir('source'):
	numFiles += 1
if numFiles < 1:
	print "No source files found. Please add source files into source folder."
	sys.exit(4)
print str(numFiles) + " Files found. Starting processing...\n"
for filename in os.listdir('source'):
	imgSource=Image.open("source/" + filename,'r')
	tmp1=ImageOps.fit(imgSource,(width, height), Image.ANTIALIAS,0,(0,0))
	imgBG_w,imgBG_h=imgBG.size
	imgBG.paste(tmp1,imgOffset)
	imgTop_w, imgTop_h=imgTop.size
	offset=((imgBG_w-imgTop_w)/2, (imgBG_h-imgTop_h)/2)
	imgBG.paste(imgTop,offset, imgTop)
	imgBG.save('output/' + filename.rsplit(".",1)[0] + '.ico')
	shutil.move("source/" + filename, "used/" + filename)
	print filename + " Done!"
print "Process complete! Completed files are in the output directory.\n"
