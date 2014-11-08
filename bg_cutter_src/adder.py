from os import listdir, remove
from os.path import isfile, join, splitext, isfile
import re
import xml.etree.ElementTree as ET

mypath = './bg/'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

for file in onlyfiles:
	fileName, fileExtension = splitext(file)
	if(fileExtension != '.xml'):
		continue
	print(fileName)
	data2 = ['<?xml version="1.0"?>\n']
	with open (mypath + file, "r") as myfile:
		data=myfile.readlines()
		for d in data:
			data2.append(d)

		#print(data2)
	with open (mypath + file, "w") as myfile:
		for d in data2:
			myfile.write(d)
